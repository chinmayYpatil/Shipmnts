from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..import database,schemas,models

router=APIRouter(tags=['Store'])

@router.post("/store",status_code=status.HTTP_201_CREATED)

def create_plan(plan:schemas.PlanCreate,db:Session=Depends(database.get_db)):
    return{"plan_id":123,"store_location":"DElhi","success":"true","message":"Plan Created succesfully"}

@router.get("/plan/{plan_id}")
def get_plan(plan_id:int,db:Session=Depends(database.get_db)):
    return{
    "plan_id":plan_id,
    "store_location":"Delhi",
    "valid_from":"2025-08-01",
    "valid_to":"2025-08-31",
    "items":[{
        "category": "veggie",
      "name": "Tomato",
      "half_price": 14,
      "full_price": 27,
      "extra_charge": 15
    }]
}