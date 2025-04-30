from fastapi import FastAPI, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session # type: ignore
from fastapi.middleware.cors import CORSMiddleware
import schemas 
from database import get_db
import models

app = FastAPI()

origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/shipments/", response_model=List[schemas.ShipmentModels])
async def create_shipment(db:db_dependency, shipments:schemas.ShipmentBase):
    db_shipments = models.Shipment(**shipments.dict())
    db.add(db_shipments)
    db.commit()
    db.refresh(db_shipments)
    return db_shipments

@app.get("/shipments/", response_model=schemas.ShipmentModels)
async def read_shipments(db:db_dependency, skip: int = 0, limit : int = 20):
    shipments = db.query(models.Shipment).offset(skip).limit(limit).all()
    return shipments
    