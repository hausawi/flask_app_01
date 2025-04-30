import datetime
from typing import Optional
from pydantic import BaseModel
import models


class ShipmentBase(BaseModel):
    tel_num: int
    email: str 
    bl_num : str
    shipper : str
    #cnee: str
    #pod: str= "Misurata"
    #pol: str= "Misurata"
    #vessel: str
    #released: bool
    #created_at: str 

class ShipmentModels(ShipmentBase):
    id: int
    class config():
        orm_mode = True

