from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr
from datetime import date, datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: str | None = None

class StoreCreate(BaseModel):
    storeLocation:str
    currency:str
    tax_percentage:str
    premium_items:List[str]

class StoreUpdate(BaseModel):
    currency:Optional[float]=None
    premium_items:Optional[List[str]]=None

class ItemDetails(BaseModel):
    category:str
    name:str
    half_price:float
    full_price:float
    extra_charge:float

class PlanCreate(BaseModel):
    store_location:str
    valid_from:date
    valid_to:date
    items:List[ItemDetails]

class PlanResponse(BaseModel):
    plan_id:int
    store_location:str
    valid_from:date
    valid_to:date
    items:List[ItemDetails]

class CalculateRequest(BaseModel):
    store_location:str
    order_date:date
    length:str
    selections:Dict[str,List[str]]
    extras:Dict[str,List[str]]

class CalculateItem(BaseModel):
    name:str
    rate:float

class CalculationRespomse(BaseModel):
    store_location:str
    currency:str
    length:str
    items:List[CalculateItem]
    total_before_tax:float
    tax_percentage:float
    total_after_tax:float


    