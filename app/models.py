from sqlalchemy import ARRAY, Column, Integer, String,Float,Boolean,ForeignKey,Date
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

class User(Base):
    """
    SQLAlchemy model for the 'users' table.
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), 
                        nullable=False, server_default=text('now()'))


class Store(Base):
    __tablename__ ="stores"
    id =Column(Integer,primary_key=True,nullable=False)
    store_location=Column(String,nullable=False,unique=True)
    currency=Column(String,nullable=False,unique=True)
    tax_percentage=Column(Float,nullable=False)
    premium_items=Column(ARRAY(String))

    # pricing_plans=relationship("PricingPlan",back_populate="Store")

    #new pricing
    class PricingPLan(Base):
        __tablename__="pricing_plans"

        id=Column(Integer,primary_key=True,nullable=False)
        store_location=Column(String,ForeignKey("stores.store_location"),nullable=False)
        valid_from=Column(Date,nullable=False)
        valid_to=Column(Date,nullable=False)
        items=Column(ARRAY(String))
        # store=relationship("Store",back_populate="pricing_plans")
    
    #new item model for pricing detail
    class Item(Base):
        __tablename__="items"
        id=Column(Integer,primary_key=True,nullable=False)
        plan_id=Column(Integer,ForeignKey("pricing_plans.id"),nullable=False)
        category=Column(String,nullable=False)
        name=Column(String,nullable=False)
        half_price=Column(Float)
        full_price=Column(Float)
        extra_charge=Column(Float)