from fastapi import APIRouter, Form
from app.services.maintenance_storage import (
    load_maintenance_items,
    load_single_maintenance_item,
    add_maintenance_item
)


router = APIRouter()


@router.get("/api/maintenance/load")
def get_all():
    m_list = load_maintenance_items()

    return {"maintenance_list": m_list}


@router.get("/api/maintenance/{id}/load")
def get_single_item(id: str):
    item_obj = load_single_maintenance_item(id)
    item_dic = item_obj.get_dict()

    return {"single_item": item_dic}

@router.post("/api/maintenance/add-item")
def add_item(name: str, ) #Keep adding to this it isn't done.
