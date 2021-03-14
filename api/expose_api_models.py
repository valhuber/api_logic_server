from safrs import SAFRSAPI

from database import models

"""
ApiLogicServer Generate From Model 01.04.11

Using Python: 3.9.1 (default, Jan 25 2021, 17:52:31) 
[Clang 12.0.0 (clang-1200.0.32.28)]

At: 2021-03-11 18:43:57.226948

"""

def expose_models(app, HOST="localhost", PORT=5000, API_PREFIX="/api"):
    """this is called by api / __init__.py"""

    api = SAFRSAPI(app, host=HOST, port=PORT)
    api.expose_object(models.Category)
    api.expose_object(models.CustomerCustomerDemo)
    api.expose_object(models.OrderDetail)
    api.expose_object(models.Order)
    api.expose_object(models.Customer)
    api.expose_object(models.CustomerDemographic)
    api.expose_object(models.EmployeeAudit)
    api.expose_object(models.EmployeeTerritory)
    api.expose_object(models.Employee)
    api.expose_object(models.Product)
    api.expose_object(models.Region)
    api.expose_object(models.Shipper)
    api.expose_object(models.Supplier)
    api.expose_object(models.Territory)
    return api
