import datetime
from decimal import Decimal
from logic_bank.exec_row_logic.logic_row import LogicRow
from logic_bank.extensions.rule_extensions import RuleExtension
from logic_bank.logic_bank import Rule


from database import models


def declare_logic():

    print("\n\ndeclare_logic")

    """ example from default database
    
    Rule.constraint(validate=models.Customer,
                    as_condition=lambda row: row.Balance <= row.CreditLimit,
                    error_msg="balance ({row.Balance}) exceeds credit ({row.CreditLimit})")
    
    use code completion to declare rules here """

    """
    This code precreated for default database, nw.sqlite.
        You would normally declare your rules, using code completion.
        For details on these rules, see https://github.com/valhuber/LogicBank/wiki/Examples

    Issues function calls to activate rules for check credit (etc), below.
        These rules are executed not now, but on commits
        Order is irrelevant - determined by system based on dependency analysis
        Their inclusion in classes is for doc / convenience, no semantics

    These rules apply to all transactions (automatic re-use), eg.
    * place order
    * change Order Detail product, quantity
    * add/delete Order Detail
    * ship / unship order
    * delete order
    * move order to new customer, etc

    These rules are automatically activated, like this

        LogicBank.activate(session=session, activator=declare_logic)
    """

    def congratulate_sales_rep(row: models.Order, old_row: models.Order, logic_row: LogicRow):
        if logic_row.ins_upd_dlt == "ins":  # logic engine fills parents for insert
            sales_rep = row.Employee
            from sqlalchemy.orm import object_mapper
            order_mapper = object_mapper(row)
            for each_descriptor in order_mapper.all_orm_descriptors:
                print(each_descriptor)
                if hasattr(each_descriptor, "key"):
                    if each_descriptor.key == "OrderDetailList":
                        how_to_make_this_sub__OrderDetail = each_descriptor.mapper
                        pass
            if sales_rep is None:
                logic_row.log("no salesrep for this order")
            else:
                 logic_row.log(f'Congratulations to {sales_rep.FirstName} on their new order')

    Rule.constraint(validate=models.Customer,
                    as_condition=lambda row: row.Balance <= row.CreditLimit,
                    error_msg="balance ({row.Balance}) exceeds credit ({row.CreditLimit})")
    Rule.sum(derive=models.Customer.Balance, as_sum_of=models.Order.AmountTotal,
             where=lambda row: row.ShippedDate is None)  # *not* a sql select sum...

    # thing = models.Order.Customer.

    Rule.sum(derive=models.Order.AmountTotal, as_sum_of=models.OrderDetail.Amount)

    Rule.formula(derive=models.OrderDetail.Amount, as_expression=lambda row: row.UnitPrice * row.Quantity)
    Rule.copy(derive=models.OrderDetail.UnitPrice, from_parent=models.Product.UnitPrice)

    Rule.commit_row_event(on_class=models.Order, calling=congratulate_sales_rep)

    Rule.formula(derive=models.OrderDetail.ShippedDate, as_exp="row.Order.ShippedDate")

    def units_in_stock(row: models.Product, old_row: models.Product, logic_row: LogicRow):
        result = row.UnitsInStock - (row.UnitsShipped - old_row.UnitsShipped)
        return result
    Rule.sum(derive=models.Product.UnitsShipped, as_sum_of=models.OrderDetail.Quantity,
             where="row.ShippedDate is not None")
    Rule.formula(derive=models.Product.UnitsInStock, calling=units_in_stock)

    Rule.count(derive=models.Customer.UnpaidOrderCount, as_count_of=models.Order,
             where=lambda row: row.ShippedDate is None)  # *not* a sql select sum...

    Rule.count(derive=models.Customer.OrderCount, as_count_of=models.Order)

    def raise_over_20_percent(row: models.Employee, old_row: models.Employee, logic_row: LogicRow):
        if logic_row.ins_upd_dlt == "upd" and row.Salary != old_row.Salary:
            return row.Salary >= Decimal('1.20') * old_row.Salary
        else:
            return True

    Rule.constraint(validate=models.Employee,
                    calling=raise_over_20_percent,
                    error_msg="{row.LastName} needs a more meaningful raise")

    def audit_by_event(row: models.Employee, old_row: models.Employee, logic_row: LogicRow):
        tedious = False  # tedious code to repeat for every audited class
        if tedious:      # see instead the following rule extension - nw_copy_row
            if logic_row.are_attributes_changed([models.Employee.Salary, models.Employee.Title]):
                copy_to_logic_row = logic_row.new_logic_row(models.EmployeeAudit)
                copy_to_logic_row.link(to_parent=logic_row)
                copy_to_logic_row.set_same_named_attributes(logic_row)
                copy_to_logic_row.insert(reason="Manual Copy " + copy_to_logic_row.name)  # triggers rules...
                # logic_row.log("audit_by_event (Manual Copy) complete")

    Rule.commit_row_event(on_class=models.Employee, calling=audit_by_event)

    RuleExtension.copy_row(copy_from=models.Employee,
                           copy_to=models.EmployeeAudit,
                           copy_when=lambda logic_row: logic_row.are_attributes_changed([models.Employee.Salary, models.Employee.Title]))

    def handle_all(logic_row: LogicRow):
        row = logic_row.row
        if logic_row.ins_upd_dlt == "ins" and hasattr(row, "CreatedOn"):
            row.CreatedOn = datetime.datetime.now()
            logic_row.log("early_row_event_all_classes - handle_all sets 'Created_on"'')

    Rule.early_row_event_all_classes(early_row_event_all_classes=handle_all)
