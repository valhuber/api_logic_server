from safrs.jsonapi import SAFRSRestAPI
from sqlalchemy.orm import relationship, backref
from database import models

"""
mimic

    Order = relationship('Order', cascade_backrefs=True, backref='OrderDetailList')
    Product = relationship('Product', cascade_backrefs=True, backref='OrderDetailList')
"""

active = False
if active:
    # models.OrderDetail = relationship('Order', cascade_backrefs=True, backref='OrderDetailList')
    # models.OrderDetail = relationship('Product', cascade_backrefs=True, backref='OrderDetailList')
    """ Mike suggests
    return relationship("Order", backref=backref("OrderDetailList"))
    """
    models.OrderDetail = relationship("Order", backref=backref("OrderDetailList"))
    models.OrderDetail._rest_api = SAFRSRestAPI