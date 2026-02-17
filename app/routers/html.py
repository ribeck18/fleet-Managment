from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from app.services.equipment_storage import load_equipment


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    """
    get and return the HTML for the home page
    
    :returns: HTML from home.jinja2
    """
    return templates.TemplateResponse(
        "home.jinja2",
        {'request': request, "equipment_list": load_equipment()}
    )