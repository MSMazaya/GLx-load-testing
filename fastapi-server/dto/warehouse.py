from pydantic import BaseModel


class WarehouseBase(BaseModel):
    name: str
    quantity: int


class WarehouseCreate(WarehouseBase):
    pass


class Warehouse(WarehouseBase):
    id: int

    class Config:
        orm_mode = True
