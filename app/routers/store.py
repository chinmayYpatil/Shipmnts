from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from ..import database,schemas,models

router=APIRouter(tags=['Store'])

@router.post("/store",status_code=status.HTTP_201_CREATED)

def create_store(store:schemas.StoreCreate,db:Session=Depends(database.get_db)):
    db_store=db.query(models.Store).filter(models.Store.store_location==store.store_location)()
    if db_store:
        raise HTTPException(status_code=status.store_location)
    new_store=models.Store(**store.dict())
    db.add(new_store)
    db.commit()
    db.refresh(new_store) 
    return{"success":True,"message":"Store created"}

@router.put("/store/{store_location}")
def update_store(store_locatiom:str,store:schemas.StoreUpdate,db:Session=Depends(database.get_db)):
    db_store=db.query(models.Store).filter(models.Store.store_location==store_locatiom)
    if not db_store.first():
        raise HTTPException(status_code=status.HTTP_404_not_found,
                            details=f"store with location{store_locatiom}not found")
    update_data=store.dict(exclude_unsent=True)
    db_store.update(update_data,synchronize_session=False)
    db.commit()
    return{"success":True,"message":"store updated"}