from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from app.services.workorder_storage import add_workorder, load_workorders, resolve, get_single_workorder

router = APIRouter()

#This route creates a workorder and returns to the main home page
@router.post("/workorders/add")
def create_workorder(title: str= Form(), info: str = Form() , user: str= Form(), severity: str= Form(), equipment: str= Form()):
    add_workorder(title, info, user, severity, equipment)
    return RedirectResponse(url="/", status_code=303)


##This causes an internal error.
@router.post("/workorders/{workorder_id}/resolve")
def resolve_workorder(workorder_id):
    resolve(workorder_id)
    return RedirectResponse(url=f"/workorders/{workorder_id}", status_code= 303)