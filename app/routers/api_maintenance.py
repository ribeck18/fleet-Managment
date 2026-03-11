from fastapi import APIRouter, Form
from app.services.maintenance_storage import load_maintenance_items


router = APIRouter()


@router.get("/api/maintenance/load")
def get_all():
    m_list = load_maintenance_items()
    return {"maintenance_list": m_list}
