from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from .deliver import Deliver  # noqa: F401

class Client(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastName = Column(String)
    cellphoneNumber = Column(Integer)
    email = Column(String)
    deliverys = relationship("Deliver", back_populates="client")