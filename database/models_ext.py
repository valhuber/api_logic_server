from types import MethodType

import sqlalchemy
from database import models
from flask_sqlalchemy import SQLAlchemy
from safrs import jsonapi_attr
from sqlalchemy import Column
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, remote, foreign, column_property

""" Objective 1 - add relationship

working, per https://docs.sqlalchemy.org/en/13/orm/join_conditions.html#specifying-alternate-join-conditions

"""

models.Employee.Manager = relationship('Employee', cascade_backrefs=True, backref='Manages',
                                       primaryjoin=remote(models.Employee.Id) ==
                                                   foreign(models.Employee.ReportsTo)
                               )
""" Objective 2 - add derived attribute

working, per Thomas' suggestion... thanks!

"""

@jsonapi_attr
def proper_salary(row):
    if not hasattr(row, "_proper_salary"):
        row._proper_salary = row.Salary + 10000  # create the attr
    return row._proper_salary

@proper_salary.setter
def proper_salary(row, value):
    row._proper_salary = value
    # print(f'_proper_salary={row._proper_salary}')
    pass

models.Employee.ProperSalary = proper_salary
# works on instance, and in swagger - success!
# no need for   # property(fget=get_proper_salary, fset=set_proper_salary)

print("models_ext.py successfully executes: models.Employee.Manager = relationship('Employee', cascade_backrefs=True, backref='Manages'")


"""
works, but taking 2 minutes.  Sql log:

DEBUG:safrs.safrs_init:sorting not implemented for Employee.proper_salary
INFO:sqlalchemy.engine.base.Engine:BEGIN (implicit)
INFO:sqlalchemy.engine.base.Engine:SELECT count(*) AS count_1
FROM (SELECT "Employee"."Id" AS "Employee_Id", "Employee"."LastName" AS "Employee_LastName", "Employee"."FirstName" AS "Employee_FirstName", "Employee"."Title" AS "Employee_Title", "Employee"."TitleOfCourtesy" AS "Employee_TitleOfCourtesy", "Employee"."BirthDate" AS "Employee_BirthDate", "Employee"."HireDate" AS "Employee_HireDate", "Employee"."Address" AS "Employee_Address", "Employee"."City" AS "Employee_City", "Employee"."Region" AS "Employee_Region", "Employee"."PostalCode" AS "Employee_PostalCode", "Employee"."Country" AS "Employee_Country", "Employee"."HomePhone" AS "Employee_HomePhone", "Employee"."Extension" AS "Employee_Extension", "Employee"."Photo" AS "Employee_Photo", "Employee"."Notes" AS "Employee_Notes", "Employee"."ReportsTo" AS "Employee_ReportsTo", "Employee"."PhotoPath" AS "Employee_PhotoPath", "Employee"."IsCommissioned" AS "Employee_IsCommissioned", "Employee"."Salary" AS "Employee_Salary"
FROM "Employee" ORDER BY "Employee"."Id", "Employee"."LastName", "Employee"."FirstName", "Employee"."Title", "Employee"."TitleOfCourtesy", "Employee"."BirthDate", "Employee"."HireDate", "Employee"."Address", "Employee"."City", "Employee"."Region", "Employee"."PostalCode", "Employee"."Country", "Employee"."HomePhone", "Employee"."Extension", "Employee"."Photo", "Employee"."Notes", "Employee"."ReportsTo", "Employee"."PhotoPath", "Employee"."IsCommissioned", "Employee"."Salary") AS anon_1
INFO:sqlalchemy.engine.base.Engine:()
INFO:sqlalchemy.engine.base.Engine:SELECT anon_1."Employee_Id" AS "anon_1_Employee_Id", anon_1."Employee_LastName" AS "anon_1_Employee_LastName", anon_1."Employee_FirstName" AS "anon_1_Employee_FirstName", anon_1."Employee_Title" AS "anon_1_Employee_Title", anon_1."Employee_TitleOfCourtesy" AS "anon_1_Employee_TitleOfCourtesy", anon_1."Employee_BirthDate" AS "anon_1_Employee_BirthDate", anon_1."Employee_HireDate" AS "anon_1_Employee_HireDate", anon_1."Employee_Address" AS "anon_1_Employee_Address", anon_1."Employee_City" AS "anon_1_Employee_City", anon_1."Employee_Region" AS "anon_1_Employee_Region", anon_1."Employee_PostalCode" AS "anon_1_Employee_PostalCode", anon_1."Employee_Country" AS "anon_1_Employee_Country", anon_1."Employee_HomePhone" AS "anon_1_Employee_HomePhone", anon_1."Employee_Extension" AS "anon_1_Employee_Extension", anon_1."Employee_Photo" AS "anon_1_Employee_Photo", anon_1."Employee_Notes" AS "anon_1_Employee_Notes", anon_1."Employee_ReportsTo" AS "anon_1_Employee_ReportsTo", anon_1."Employee_PhotoPath" AS "anon_1_Employee_PhotoPath", anon_1."Employee_IsCommissioned" AS "anon_1_Employee_IsCommissioned", anon_1."Employee_Salary" AS "anon_1_Employee_Salary", "Employee_1"."Id" AS "Employee_1_Id", "Employee_1"."LastName" AS "Employee_1_LastName", "Employee_1"."FirstName" AS "Employee_1_FirstName", "Employee_1"."Title" AS "Employee_1_Title", "Employee_1"."TitleOfCourtesy" AS "Employee_1_TitleOfCourtesy", "Employee_1"."BirthDate" AS "Employee_1_BirthDate", "Employee_1"."HireDate" AS "Employee_1_HireDate", "Employee_1"."Address" AS "Employee_1_Address", "Employee_1"."City" AS "Employee_1_City", "Employee_1"."Region" AS "Employee_1_Region", "Employee_1"."PostalCode" AS "Employee_1_PostalCode", "Employee_1"."Country" AS "Employee_1_Country", "Employee_1"."HomePhone" AS "Employee_1_HomePhone", "Employee_1"."Extension" AS "Employee_1_Extension", "Employee_1"."Photo" AS "Employee_1_Photo", "Employee_1"."Notes" AS "Employee_1_Notes", "Employee_1"."ReportsTo" AS "Employee_1_ReportsTo", "Employee_1"."PhotoPath" AS "Employee_1_PhotoPath", "Employee_1"."IsCommissioned" AS "Employee_1_IsCommissioned", "Employee_1"."Salary" AS "Employee_1_Salary", "Employee_2"."Id" AS "Employee_2_Id", "Employee_2"."LastName" AS "Employee_2_LastName", "Employee_2"."FirstName" AS "Employee_2_FirstName", "Employee_2"."Title" AS "Employee_2_Title", "Employee_2"."TitleOfCourtesy" AS "Employee_2_TitleOfCourtesy", "Employee_2"."BirthDate" AS "Employee_2_BirthDate", "Employee_2"."HireDate" AS "Employee_2_HireDate", "Employee_2"."Address" AS "Employee_2_Address", "Employee_2"."City" AS "Employee_2_City", "Employee_2"."Region" AS "Employee_2_Region", "Employee_2"."PostalCode" AS "Employee_2_PostalCode", "Employee_2"."Country" AS "Employee_2_Country", "Employee_2"."HomePhone" AS "Employee_2_HomePhone", "Employee_2"."Extension" AS "Employee_2_Extension", "Employee_2"."Photo" AS "Employee_2_Photo", "Employee_2"."Notes" AS "Employee_2_Notes", "Employee_2"."ReportsTo" AS "Employee_2_ReportsTo", "Employee_2"."PhotoPath" AS "Employee_2_PhotoPath", "Employee_2"."IsCommissioned" AS "Employee_2_IsCommissioned", "Employee_2"."Salary" AS "Employee_2_Salary", "EmployeeAudit_1"."Id" AS "EmployeeAudit_1_Id", "EmployeeAudit_1"."Title" AS "EmployeeAudit_1_Title", "EmployeeAudit_1"."Salary" AS "EmployeeAudit_1_Salary", "EmployeeAudit_1"."LastName" AS "EmployeeAudit_1_LastName", "EmployeeAudit_1"."FirstName" AS "EmployeeAudit_1_FirstName", "EmployeeAudit_1"."EmployeeId" AS "EmployeeAudit_1_EmployeeId", "EmployeeAudit_1"."CreatedOn" AS "EmployeeAudit_1_CreatedOn", "EmployeeTerritory_1"."Id" AS "EmployeeTerritory_1_Id", "EmployeeTerritory_1"."EmployeeId" AS "EmployeeTerritory_1_EmployeeId", "EmployeeTerritory_1"."TerritoryId" AS "EmployeeTerritory_1_TerritoryId", "Order_1"."Id" AS "Order_1_Id", "Order_1"."CustomerId" AS "Order_1_CustomerId", "Order_1"."EmployeeId" AS "Order_1_EmployeeId", "Order_1"."OrderDate" AS "Order_1_OrderDate", "Order_1"."RequiredDate" AS "Order_1_RequiredDate", "Order_1"."ShippedDate" AS "Order_1_ShippedDate", "Order_1"."ShipVia" AS "Order_1_ShipVia", "Order_1"."Freight" AS "Order_1_Freight", "Order_1"."ShipName" AS "Order_1_ShipName", "Order_1"."ShipAddress" AS "Order_1_ShipAddress", "Order_1"."ShipCity" AS "Order_1_ShipCity", "Order_1"."ShipRegion" AS "Order_1_ShipRegion", "Order_1"."ShipPostalCode" AS "Order_1_ShipPostalCode", "Order_1"."ShipCountry" AS "Order_1_ShipCountry", "Order_1"."AmountTotal" AS "Order_1_AmountTotal"
FROM (SELECT "Employee"."Id" AS "Employee_Id", "Employee"."LastName" AS "Employee_LastName", "Employee"."FirstName" AS "Employee_FirstName", "Employee"."Title" AS "Employee_Title", "Employee"."TitleOfCourtesy" AS "Employee_TitleOfCourtesy", "Employee"."BirthDate" AS "Employee_BirthDate", "Employee"."HireDate" AS "Employee_HireDate", "Employee"."Address" AS "Employee_Address", "Employee"."City" AS "Employee_City", "Employee"."Region" AS "Employee_Region", "Employee"."PostalCode" AS "Employee_PostalCode", "Employee"."Country" AS "Employee_Country", "Employee"."HomePhone" AS "Employee_HomePhone", "Employee"."Extension" AS "Employee_Extension", "Employee"."Photo" AS "Employee_Photo", "Employee"."Notes" AS "Employee_Notes", "Employee"."ReportsTo" AS "Employee_ReportsTo", "Employee"."PhotoPath" AS "Employee_PhotoPath", "Employee"."IsCommissioned" AS "Employee_IsCommissioned", "Employee"."Salary" AS "Employee_Salary"
FROM "Employee" ORDER BY "Employee"."Id", "Employee"."LastName", "Employee"."FirstName", "Employee"."Title", "Employee"."TitleOfCourtesy", "Employee"."BirthDate", "Employee"."HireDate", "Employee"."Address", "Employee"."City", "Employee"."Region", "Employee"."PostalCode", "Employee"."Country", "Employee"."HomePhone", "Employee"."Extension", "Employee"."Photo", "Employee"."Notes", "Employee"."ReportsTo", "Employee"."PhotoPath", "Employee"."IsCommissioned", "Employee"."Salary"
 LIMIT ? OFFSET ?) AS anon_1 LEFT OUTER JOIN "Employee" AS "Employee_1" ON "Employee_1"."Id" = anon_1."Employee_ReportsTo" LEFT OUTER JOIN "Employee" AS "Employee_2" ON anon_1."Employee_Id" = "Employee_2"."ReportsTo" LEFT OUTER JOIN "EmployeeAudit" AS "EmployeeAudit_1" ON anon_1."Employee_Id" = "EmployeeAudit_1"."EmployeeId" LEFT OUTER JOIN "EmployeeTerritory" AS "EmployeeTerritory_1" ON anon_1."Employee_Id" = "EmployeeTerritory_1"."EmployeeId" LEFT OUTER JOIN "Order" AS "Order_1" ON anon_1."Employee_Id" = "Order_1"."EmployeeId" ORDER BY anon_1."Employee_Id", anon_1."Employee_LastName", anon_1."Employee_FirstName", anon_1."Employee_Title", anon_1."Employee_TitleOfCourtesy", anon_1."Employee_BirthDate", anon_1."Employee_HireDate", anon_1."Employee_Address", anon_1."Employee_City", anon_1."Employee_Region", anon_1."Employee_PostalCode", anon_1."Employee_Country", anon_1."Employee_HomePhone", anon_1."Employee_Extension", anon_1."Employee_Photo", anon_1."Employee_Notes", anon_1."Employee_ReportsTo", anon_1."Employee_PhotoPath", anon_1."Employee_IsCommissioned", anon_1."Employee_Salary"
INFO:sqlalchemy.engine.base.Engine:(10, 0)
INFO:sqlalchemy.engine.base.Engine:COMMIT

"""
