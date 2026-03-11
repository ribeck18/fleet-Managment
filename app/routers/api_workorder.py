from fastapi import APIRouter, Form
from app.services.workorder_storage import add_workorder, load_workorders, resolve

router = APIRouter()

#Load all of the workorders from the json file
@router.get("/api/workorder/list")
def load_workorders():
    data = load_workorders()
    return {"workorders": data}

#Create a new workorder and add it to the json file
@router.post("/api/workorders/add")
def create_workorder(title: str= Form(), info: str = Form() , user: str= Form(), severity: str= Form(), equipment: str= Form()):
    new = add_workorder(title, info, user, severity, equipment)
    return {"new_workorder": new}

#Resolve a workorder -- typically would use patch rather than post but html only supports get and post
@router.patch("/api/workorders/{workorder_id}/resolve")
def resolve_workorder(workorder_id):
    resolved_workorder = resolve(workorder_id)
    return {"workorder resolved": resolved_workorder}
