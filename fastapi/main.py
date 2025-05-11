from fastapi import FastAPI, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session # type: ignore
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import Base, SessionLocal, engine
import models

app = FastAPI()

origins = [
    'http://localhost:3000',
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ShipmentBase(BaseModel):
    email: str 
    bl_num : str
    shipper : str
    is_released : bool
    created_at: str 

class ShipmentModels(ShipmentBase):
    id: int
    class config():
        orm_mode = True


db_dependency = Annotated[Session, Depends(get_db)]

Base.metadata.create_all(bind=engine)


@app.post("/shipments/", response_model=ShipmentModels)
async def create_shipment(db:db_dependency, shipments:ShipmentBase):
    db_shipments = models.Shipment(**shipments.model_dump())
    db.add(db_shipments)
    db.commit()
    db.refresh(db_shipments)
    return db_shipments

@app.get("/shipments/", response_model=List[ShipmentModels])
async def read_shipments(db:db_dependency, skip: int = 0, limit : int = 20):
    shipments = db.query(models.Shipment).offset(skip).limit(limit).all()
    return shipments
    

