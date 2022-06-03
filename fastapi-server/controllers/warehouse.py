from typing import Union, List
from fastapi import APIRouter, Depends
from models.database import get_db
from sqlalchemy.orm import Session
import dto
import repository

router = APIRouter(prefix="/warehouse")


@router.get("/", response_model=List[dto.Warehouse])
def get_warehouses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    db_warehouse = repository.get_warehouses(db, skip, limit)
    return db_warehouse


@router.get("/{warehouse_id}")
def get_warehouse_by_id(warehouse_id: int, db: Session = Depends(get_db)):
    db_user = repository.get_warehouse(db, warehouse_id)
    return db_user


@router.post("/", response_model=dto.Warehouse)
def create_warehouse(warehouse: dto.WarehouseCreate, db: Session = Depends(get_db)):
    db_warehouse = repository.warehouse.create_warehouse(db, warehouse)
    return db_warehouse
