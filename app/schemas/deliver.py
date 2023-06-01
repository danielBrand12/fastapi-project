from typing import Optional

from pydantic import BaseModel


# Shared properties
class DeliverBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on Deliver creation
class DeliverCreate(DeliverBase):
    title: str


# Properties to receive on Deliver update
class DeliverUpdate(DeliverBase):
    pass


# Properties shared by models stored in DB
class DeliverInDBBase(DeliverBase):
    id: int
    title: str
    #owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Deliver(DeliverInDBBase):
    pass


# Properties properties stored in DB
class DeliverInDB(DeliverInDBBase):
    pass