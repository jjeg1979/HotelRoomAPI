from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBCustomer

from hotel.operations.customers import (
    CustomerCreateData,
    CustomerUpdateData,
    delete_customer,
    read_all_customers,
    read_customer,
    create_customer,
    update_customer,
)

router = APIRouter()   # type: ignore


@router.get("/customers")  # type: ignore
def api_red_all_customers():
    customer_interface = DBInterface(DBCustomer)
    return read_all_customers(customer_interface)


@router.get("/customer/{customer_id}")  # type: ignore
def api_read_customer(customer_id: int):
    customer_interface = DBInterface(DBCustomer)
    return read_customer(customer_id, customer_interface)


@router.post("/customer")  # type: ignore
def api_create_customer(customer: CustomerCreateData):
    customer_interface = DBInterface(DBCustomer)
    return create_customer(customer, customer_interface)


@router.post("/customer/{customer_id}")  # type: ignore
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    customer_interface = DBInterface(DBCustomer)
    return update_customer(customer_id, customer, customer_interface)


@router.delete("/customer/{customer_id}")  # type: ignore
def api_delete_customer(customer_id: int):
    customer_interface = DBInterface(DBCustomer)
    return delete_customer(customer_id, customer_interface)
