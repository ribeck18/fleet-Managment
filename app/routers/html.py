from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.services.equipment_storage import load_equipment, load_single_equipment_dict
from app.services.workorder_storage import load_workorders, get_equip_workorders


router = APIRouter()
templates = Jinja2Templates(directory="templates")

#Home page of the website
@router.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    """
    get and return the HTML for the home page
    
    :returns: HTML from home.jinja2
    """
    return templates.TemplateResponse(
        "home.jinja2",
        {'request': request, "equipment_list": load_equipment(), "workorder_list": load_workorders()}
    )

#Equipment page of the website
@router.get("/equipment", response_class=HTMLResponse)
def equipment_page(request: Request):
    
    return templates.TemplateResponse(
        "equipment-page.jinja2",
        {'request': request, "equipment_list": load_equipment()}
    )

#Equipment detail page
@router.get("/equipment/{equip_id}")
def equipment_detail(request: Request, equip_id: str):
    equipment = load_single_equipment_dict(equip_id)
    workorders = get_equip_workorders(equip_id)
    
    return templates.TemplateResponse(
        "equipment-detail.jinja2",
        {
            'request': request, 
            "equipment": equipment,
            "workorders": workorders
        }
    )
