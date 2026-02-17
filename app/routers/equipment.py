from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from app.services.equipment_storage import load_equipment, create_equipment, load_single_equipment


router = APIRouter()

#Create equipment 
@router.post("/api/equipment/new")
def new_equipment(
    name: str = Form(), 
    year: str = Form(), 
    status: str = Form(), 
    notes: str = Form("")
): 
    new = create_equipment(name, year, status, notes)
    return RedirectResponse(url="/", status_code=303)

#Get equipment list
@router.get("/api/equipment/list")
def get_equipment():
    return {"List": load_equipment()}

#Get a single equipment item.
@router.get("/api/equipment/{uuid}")
def get_item(uuid: str):
    item = load_single_equipment(uuid)

    return {"equipment": item}






    
