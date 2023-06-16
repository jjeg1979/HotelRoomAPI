from typing import Optional
from hotel.operations.interface import DataInterface, DataObject
from pydantic import BaseModel


class CustomerCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str


class CustomerUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email_address: Optional[str]


def read_all_customers(customer_interface: DataInterface) -> list[DataObject]:
    return customer_interface.read_all()


def read_customer(customer_id: int, customer_interface: DataInterface) -> DataObject:
    return customer_interface.read_by_id(customer_id)


def create_customer(data: CustomerCreateData, customer_interface: DataInterface) -> DataObject:
    return customer_interface.create(data)


def update_customer(customer_id: int, data: CustomerUpdateData, customer_interface: DataInterface) -> DataObject:
    return customer_interface.update(customer_id, data)


def delete_customer(customer_id: int, customer_interface: DataInterface) -> DataObject:
    return customer_interface.delete(customer_id)
