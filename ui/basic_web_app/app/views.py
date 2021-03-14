"""
ApiLogicServer Generate From Model 01.04.11

Using Python: 3.9.1 (default, Jan 25 2021, 17:52:31) 
[Clang 12.0.0 (clang-1200.0.32.28)]

Favorites: ['name', 'description']

Non Favorites: ['id']

At: 2021-03-11 18:43:57.226884

"""

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from database.models import *



class CategoryModelView(ModelView):
   datamodel = SQLAInterface(Category)
   list_columns = ["CategoryName", "Description"]
   show_columns = ["CategoryName", "Description", "Id"]
   edit_columns = ["CategoryName", "Description", "Id"]
   add_columns = ["CategoryName", "Description", "Id"]
   related_views = []

appbuilder.add_view(
      CategoryModelView, "Category List", icon="fa-folder-open-o", category="Menu")





class CustomerCustomerDemoModelView(ModelView):
   datamodel = SQLAInterface(CustomerCustomerDemo)
   list_columns = ["Id", "Customer.CompanyName"]
   show_columns = ["Id", "Customer.CompanyName", "CustomerTypeId"]
   edit_columns = ["Id", "CustomerTypeId"]
   add_columns = ["Id", "CustomerTypeId"]
   related_views = []

appbuilder.add_view(
      CustomerCustomerDemoModelView, "CustomerCustomerDemo List", icon="fa-folder-open-o", category="Menu")





class OrderDetailModelView(ModelView):
   datamodel = SQLAInterface(OrderDetail)
   list_columns = [
"Id", "Order.ShipName", "Product.ProductName", "UnitPrice", "Quantity"]
   show_columns = [
"Id", "Order.ShipName", "Product.ProductName", "UnitPrice", "Quantity", "Discount", "Amount", "ShippedDate", "ProductId", "OrderId"]
   edit_columns = [
"Id", "UnitPrice", "Quantity", "Discount", "Amount", "ShippedDate", "ProductId", "OrderId"]
   add_columns = [
"Id", "UnitPrice", "Quantity", "Discount", "Amount", "ShippedDate", "ProductId", "OrderId"]
   related_views = []

appbuilder.add_view(
      OrderDetailModelView, "OrderDetail List", icon="fa-folder-open-o", category="Menu")





class OrderModelView(ModelView):
   datamodel = SQLAInterface(Order)
   list_columns = ["ShipName", "Customer.CompanyName", "Employee.LastName", "OrderDate", "RequiredDate"]
   show_columns = ["ShipName", "Customer.CompanyName", "Employee.LastName", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "AmountTotal", "EmployeeId", "CustomerId", "Id"]
   edit_columns = ["ShipName", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "AmountTotal", "EmployeeId", "CustomerId", "Id"]
   add_columns = ["ShipName", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry", "AmountTotal", "EmployeeId", "CustomerId", "Id"]
   related_views = []  # omitted mutually referring relationships: Order 

appbuilder.add_view(
      OrderModelView, "Order List", icon="fa-folder-open-o", category="Menu")





class CustomerModelView(ModelView):
   datamodel = SQLAInterface(Customer)
   list_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City"]
   show_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "Balance", "CreditLimit", "OrderCount", "UnpaidOrderCount", "Id"]
   edit_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "Balance", "CreditLimit", "OrderCount", "UnpaidOrderCount", "Id"]
   add_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "Balance", "CreditLimit", "OrderCount", "UnpaidOrderCount", "Id"]
   related_views = []  # omitted mutually referring relationships: Customer Customer 

appbuilder.add_view(
      CustomerModelView, "Customer List", icon="fa-folder-open-o", category="Menu")





class CustomerDemographicModelView(ModelView):
   datamodel = SQLAInterface(CustomerDemographic)
   list_columns = ["Id", "CustomerDesc"]
   show_columns = ["Id", "CustomerDesc"]
   edit_columns = ["Id", "CustomerDesc"]
   add_columns = ["Id", "CustomerDesc"]
   related_views = []

appbuilder.add_view(
      CustomerDemographicModelView, "CustomerDemographic List", icon="fa-folder-open-o", category="Menu")





class EmployeeAuditModelView(ModelView):
   datamodel = SQLAInterface(EmployeeAudit)
   list_columns = ["LastName", "Employee.LastName", "Title", "Salary", "FirstName"]
   show_columns = ["LastName", "Employee.LastName", "Title", "Salary", "FirstName", "CreatedOn", "EmployeeId", "Id"]
   edit_columns = ["LastName", "Title", "Salary", "FirstName", "CreatedOn", "EmployeeId", "Id"]
   add_columns = ["LastName", "Title", "Salary", "FirstName", "CreatedOn", "EmployeeId", "Id"]
   related_views = []

appbuilder.add_view(
      EmployeeAuditModelView, "EmployeeAudit List", icon="fa-folder-open-o", category="Menu")





class EmployeeTerritoryModelView(ModelView):
   datamodel = SQLAInterface(EmployeeTerritory)
   list_columns = ["Id", "Employee.LastName", "Territory.TerritoryDescription"]
   show_columns = ["Id", "Employee.LastName", "Territory.TerritoryDescription", "EmployeeId", "TerritoryId"]
   edit_columns = ["Id", "EmployeeId", "TerritoryId"]
   add_columns = ["Id", "EmployeeId", "TerritoryId"]
   related_views = []

appbuilder.add_view(
      EmployeeTerritoryModelView, "EmployeeTerritory List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: Order



class EmployeeModelView(ModelView):
   datamodel = SQLAInterface(Employee)
   list_columns = ["LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate"]
   show_columns = ["LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath", "IsCommissioned", "Salary", "Id"]
   edit_columns = ["LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath", "IsCommissioned", "Salary", "Id"]
   add_columns = ["LastName", "FirstName", "Title", "TitleOfCourtesy", "BirthDate", "HireDate", "Address", "City", "Region", "PostalCode", "Country", "HomePhone", "Extension", "Photo", "Notes", "ReportsTo", "PhotoPath", "IsCommissioned", "Salary", "Id"]
   related_views = []  # omitted mutually referring relationships: Employee Employee Employee 

appbuilder.add_view(
      EmployeeModelView, "Employee List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: OrderDetail



class ProductModelView(ModelView):
   datamodel = SQLAInterface(Product)
   list_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder"]
   show_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "UnitsShipped", "SupplierId", "CategoryId", "Id"]
   edit_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "UnitsShipped", "SupplierId", "CategoryId", "Id"]
   add_columns = ["ProductName", "QuantityPerUnit", "UnitPrice", "UnitsInStock", "UnitsOnOrder", "ReorderLevel", "Discontinued", "UnitsShipped", "SupplierId", "CategoryId", "Id"]
   related_views = []  # omitted mutually referring relationships: Product 

appbuilder.add_view(
      ProductModelView, "Product List", icon="fa-folder-open-o", category="Menu")


# not_exposed: api.expose_object(models.{table_name})


class RegionModelView(ModelView):
   datamodel = SQLAInterface(Region)
   list_columns = ["RegionDescription"]
   show_columns = ["RegionDescription", "Id"]
   edit_columns = ["RegionDescription", "Id"]
   add_columns = ["RegionDescription", "Id"]
   related_views = []

appbuilder.add_view(
      RegionModelView, "Region List", icon="fa-folder-open-o", category="Menu")





class ShipperModelView(ModelView):
   datamodel = SQLAInterface(Shipper)
   list_columns = ["CompanyName", "Phone"]
   show_columns = ["CompanyName", "Phone", "Id"]
   edit_columns = ["CompanyName", "Phone", "Id"]
   add_columns = ["CompanyName", "Phone", "Id"]
   related_views = []

appbuilder.add_view(
      ShipperModelView, "Shipper List", icon="fa-folder-open-o", category="Menu")





class SupplierModelView(ModelView):
   datamodel = SQLAInterface(Supplier)
   list_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City"]
   show_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage", "Id"]
   edit_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage", "Id"]
   add_columns = ["CompanyName", "ContactName", "ContactTitle", "Address", "City", "Region", "PostalCode", "Country", "Phone", "Fax", "HomePage", "Id"]
   related_views = []

appbuilder.add_view(
      SupplierModelView, "Supplier List", icon="fa-folder-open-o", category="Menu")


# table already generated per recursion: EmployeeTerritory



class TerritoryModelView(ModelView):
   datamodel = SQLAInterface(Territory)
   list_columns = ["TerritoryDescription"]
   show_columns = ["TerritoryDescription", "Id", "RegionId"]
   edit_columns = ["TerritoryDescription", "Id", "RegionId"]
   add_columns = ["TerritoryDescription", "Id", "RegionId"]
   related_views = []  # omitted mutually referring relationships: Territory 

appbuilder.add_view(
      TerritoryModelView, "Territory List", icon="fa-folder-open-o", category="Menu")


# skip admin table: ab_permission
# skip admin table: ab_register_user
# skip admin table: ab_role
# skip admin table: ab_user
# skip admin table: ab_view_menu
# skip sqlite_sequence table: sqlite_sequence
# table already generated per recursion: CustomerCustomerDemo
# table already generated per recursion: EmployeeAudit
# table already generated per recursion: EmployeeTerritory
# table already generated per recursion: Order
# skip admin table: ab_permission_view
# skip admin table: ab_user_role
# table already generated per recursion: OrderDetail
# skip admin table: ab_permission_view_role
#  24 table(s) in model; generated 14 page(s), including 0 related_view(s).

#  Warning - no related_views, since foreign keys missing
#  .. add them to your models.py (see nw example)
#  .. or better, add them to your database