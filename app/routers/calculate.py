from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..import database,schemas,models

router=APIRouter(tags=['Price Calculation'])

@router.post("/calculate")
def calculate_price(request:schemas.CalculateRequest,db:Session=Depends(database.get_db)):
    return{
  "store_location": "Mumbai",
  "order_date": "2025-07-10",
  "length": "full",
  "selections": {
    "bread": ["Italian"],
    "sauce": ["Mayo", "BBQ"],
    "veggie": ["Lettuce", "Tomato"]
  },
  "extras": {
    "sauce": ["Mayo"],
    "veggie": ["Tomato","Lettuce"]
  }
}
