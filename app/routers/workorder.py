from fastapi import APIRouter
from app.services.workorder_storage import add_workorder, load_workorders

router = APIRouter()

#Load all of the workorders from the json file
@router.get("/api/workorder/list")
def load_workorders():
    data = load_workorders()
    return {"workorders": data}

#Create a new workorder and add it to the json file
@router.post("/api/workorders/add")
def create_workorder(workorder: dict):
    add_workorder(dict)
    return {"status": f"created{workorder}"}
