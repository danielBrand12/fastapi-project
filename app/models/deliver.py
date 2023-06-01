from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from .client import Client  # noqa: F401

class Deliver(Base):
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)  # Dirección de entrega
    city = Column(String)     # Ciudad
    state = Column(String)    # Estado o provincia
    client_id = Column(Integer, ForeignKey("Client.id"))
    client = relationship("Client", back_populates="deliverys")
