from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps


router = APIRouter()

@router.get("/", response_model=List[schemas.Client])
def read_client(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve clients.
    """
    clients = crud.client.get_multi(db, skip=skip, limit=limit)
    return clients


@router.post("/", response_model=schemas.Client)
def create_client(
    *,
    db: Session = Depends(deps.get_db),
    client_in: schemas.ClientCreate,
) -> Any:
    """
    Create new client.
    """
    client = crud.client.create(db=db, obj_in=client_in)
    return client


@router.put("/{id}", response_model=schemas.Client)
def update_client(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    client_in: schemas.ClientUpdate,
) -> Any:
    """
    Update an client.
    """
    client = crud.client.get(db=db, id=id)
    if not client:
        raise HTTPException(status_code=404, detail="client not found")
    client = crud.client.update(db=db, db_obj=client, obj_in=client_in)
    return client


@router.get("/{id}", response_model=schemas.Client)
def read_client(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get client by ID.
    """
    client = crud.client.get(db=db, id=id)
    if not client:
        raise HTTPException(status_code=404, detail="client not found")
    return client


@router.delete("/{id}", response_model=schemas.Client)
def delete_client(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an client.
    """
    client = crud.client.get(db=db, id=id)
    if not client:
        raise HTTPException(status_code=404, detail="client not found")
    client = crud.client.remove(db=db, id=id)
    return client