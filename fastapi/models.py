from database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer, Float, Boolean, text

class Shipment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    bl_num = Column(String)
    shipper = Column(String)
    is_released = Column(Boolean)
    created_at = Column(String)  #(TIMESTAMP(timezone=True), server_default=text('now()'))




