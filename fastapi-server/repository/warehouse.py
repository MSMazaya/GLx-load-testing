from sqlalchemy.orm import Session

import dto
import models


def get_warehouse(db: Session, warehouse_id: int):
    return db.query(models.Warehouse).filter(models.Warehouse.id == warehouse_id).first()


def get_warehouses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Warehouse).offset(skip).limit(limit).all()


def create_warehouse(db: Session, warehouse: dto.WarehouseCreate):
    db_warehouse = models.Warehouse(
        name=warehouse.name, quantity=warehouse.quantity)
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse
