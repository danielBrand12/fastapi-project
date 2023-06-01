from typing import Optional

from pydantic import BaseModel


# Shared properties
class DeliverBase(BaseModel):
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None


# Properties to receive on Deliver creation
class DeliverCreate(DeliverBase):
    address: str


# Properties to receive on Deliver update
class DeliverUpdate(DeliverBase):
    pass


# Properties shared by models stored in DB
class DeliverInDBBase(DeliverBase):
    id: int
    address: str
    client_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Deliver(DeliverInDBBase):
    pass


# Properties properties stored in DB
class DeliverInDB(DeliverInDBBase):
    pass