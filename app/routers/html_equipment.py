from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from app.services.equipment_storage import load_equipment, create_equipment, load_single_equipment_dict, Load_single_equipment_object
from classes.Equipment import Equipment

router = APIRouter()

#This route is for the add equipment button on the main page.
@router.post("/equipment/new")
def new_equipment(
    name: str = Form(), 
    year: str = Form(), 
    status: str = Form(), 
    notes: str = Form("")
): 
    create_equipment(name, year, status, notes)
    return RedirectResponse(url="/", status_code=303)

