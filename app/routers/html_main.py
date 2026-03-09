from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.services.equipment_storage import load_equipment, load_single_equipment_dict
from app.services.workorder_storage import load_workorders, get_equip_workorders, get_equipment, get_single_workorder


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

#Work orders page
@router.get("/workorders", response_class=HTMLResponse)
def workorder_page(request: Request):

    return templates.TemplateResponse(
        "workorder-page.jinja2",
        {"request": request, "workorder_list": load_workorders()}
    )


#Work order detail page
@router.get("/workorders/{workorder_id}")
def workorder_detail(request: Request, workorder_id):
    workorder = get_single_workorder(workorder_id)
    equipment = get_equipment(workorder_id)

    return templates.TemplateResponse(
        "workorder-detail.jinja2",
        {"request": request,
        "equipment": equipment,
         "workorder": workorder}
    )

# This is for the new home page
@router.get("/home", response_class=HTMLResponse)
def temp_home_page(request: Request):
    """
    get and return the HTML for the home page
    
    :returns: HTML from home.jinja2
    """
    return templates.TemplateResponse(
        "new-home.jinja2",
        {'request': request}
    )
