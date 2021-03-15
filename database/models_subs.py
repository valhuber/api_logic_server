# coding: utf-8

# to pursue super/subs, rename this to models.py

from sqlalchemy.ext.hybrid import hybrid_property

from database import models_base


class Category(models_base.Category_base):
    pass


class Customer(models_base.Customer_base):
    pass


class CustomerDemographic(models_base.CustomerDemographic_base):
    pass


class Employee(models_base.Employee_base):
    pass


class Product(models_base.Product_base):
    pass


class Region(models_base.Region_base):
    pass


class Shipper(models_base.Shipper_base):
    pass


class Supplier(models_base.Supplier_base):
    pass


class Territory(models_base.Territory_base):
    pass


class AbPermission(models_base.AbPermission_base):
    pass


class AbRegisterUser(models_base.AbRegisterUser_base):
    pass


class AbRole(models_base.AbRole_base):
    pass


class AbUser(models_base.AbUser_base):
    pass


class AbViewMenu(models_base.AbViewMenu_base):
    pass


class CustomerCustomerDemo(models_base.CustomerCustomerDemo_base):
    pass


class EmployeeAudit(models_base.EmployeeAudit_base):
    pass


class EmployeeTerritory(models_base.EmployeeTerritory_base):
    pass


class Order(models_base.Order_base):
    pass

    @hybrid_property
    def order_count(self):
        if not hasattr(self, "_order_count"):
            self._order_count = 11
        return self._order_count

    @order_count.setter
    def order_count(self, value):
        self._order_count = value



class AbPermissionView(models_base.AbPermissionView_base):
    pass


class AbUserRole(models_base.AbUserRole_base):
    pass


class OrderDetail(models_base.OrderDetail_base):
    pass


class AbPermissionViewRole(models_base.AbPermissionViewRole_base):
    pass


from database import models_relns
