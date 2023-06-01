from app.crud.base import CRUDBase
from app.models.deliver import Deliver
from app.schemas.deliver import DeliverCreate, DeliverUpdate


class CRUDDeliver(CRUDBase[Deliver, DeliverCreate, DeliverUpdate]):
    ... 


deliver = CRUDDeliver(Deliver)