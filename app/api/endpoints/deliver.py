from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps


router = APIRouter()

@router.get("/", response_model=List[schemas.Deliver])
def read_deliver(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve delivers.
    """
    delivers = crud.deliver.get_multi(db, skip=skip, limit=limit)
    return delivers


@router.post("/", response_model=schemas.Deliver)
def create_deliver(
    *,
    db: Session = Depends(deps.get_db),
    deliver_in: schemas.DeliverCreate,
) -> Any:
    """
    Create new deliver.
    """
    deliver = crud.deliver.create(db=db, obj_in=deliver_in)
    return deliver


@router.put("/{id}", response_model=schemas.Deliver)
def update_deliver(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    deliver_in: schemas.DeliverUpdate,
) -> Any:
    """
    Update an deliver.
    """
    deliver = crud.deliver.get(db=db, id=id)
    if not deliver:
        raise HTTPException(status_code=404, detail="deliver not found")
    deliver = crud.deliver.update(db=db, db_obj=deliver, obj_in=deliver_in)
    return deliver


@router.get("/{id}", response_model=schemas.Deliver)
def read_deliver(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get deliver by ID.
    """
    deliver = crud.deliver.get(db=db, id=id)
    if not deliver:
        raise HTTPException(status_code=404, detail="deliver not found")
    return deliver


@router.delete("/{id}", response_model=schemas.Deliver)
def delete_deliver(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an deliver.
    """
    deliver = crud.deliver.get(db=db, id=id)
    if not deliver:
        raise HTTPException(status_code=404, detail="deliver not found")
    deliver = crud.deliver.remove(db=db, id=id)
    return deliver