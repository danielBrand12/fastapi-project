from typing import Optional

from pydantic import BaseModel


# Shared properties
class ClientBase(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    cellphoneNumber: Optional[int] = None
    email: Optional[str] = None


# Properties to receive on Client creation
class ClientCreate(ClientBase):
    name: str


# Properties to receive on Client update
class ClientUpdate(ClientBase):
    pass


# Properties shared by models stored in DB
class ClientInDBBase(ClientBase):
    id: int
    name: str
    #owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Client(ClientInDBBase):
    pass


# Properties properties stored in DB
class ClientInDB(ClientInDBBase):
    pass