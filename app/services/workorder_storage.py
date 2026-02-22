import json
from pathlib import Path
from classes.WorkOrders import WorkOrder
from app.services.equipment_storage import Load_single_equipment_object

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "workorders_data.json"

def load_workorders():
    """
    loads all work orders from json

    :return: List of work orders as dictionaries
    """
    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        data = []
    
    return data

def save_workorder(workorders: dict):
    """
    adds workorder dict to the json file.
    
    :param workorders: workorder info
    :type workorders: dict
    """
    with open(DATA_PATH, "w") as f:
        json.dump(workorders, f, indent=4, default=str)

    return 

def add_workorder(title: str, info: str, user: str, severity: str, equipment: str):
    """
    Create a new workorder object and append it to the data file
    
    :param title: workorder title
    :type title: str
    :param info: workorder info
    :type info: str
    :param user: user that made workorder
    :type user: str
    :param severity: workorder severity
    :type severity: str
    :param equipment: uuid of the associated equipment item.
    :type equipment: str

    :return: new workorder object
    """
    workorder = WorkOrder(title, info, user, severity, equipment)

    workorders = load_workorders()
    workorders.append(workorder.get_dict())
    save_workorder(workorders)

    return workorder

def get_equip_workorders(equip_id: str):
    """
    Load all work orders, compare the equip_id to the Equipment uuid stored on each list. Append each matching workorder to a list of workorders
    
    :param equip_id: Equipment UUID
    :type equip_id: str

    :return: List of work order dictionaries
    """
    all_workorders = load_workorders()

    workorders = []

    for i in all_workorders:
        equipment = i.get("equipment")

        if equip_id == equipment:
            workorders.append(i)
    
    #check if any work orders were found
    if workorders == []:
        return []
    
    return workorders

def get_single_workorder(workorder_id: str):
    workorders = load_workorders()

    for i in workorders:
        i_id = i["id"]

        if i_id == workorder_id:
            workorder = i
    return workorder

#Get the equipment item associated with the workorder.
def get_equipment(workorder_id):
    workorder_list = load_workorders()

    for item in workorder_list:
        item_id = item["id"]

        if workorder_id == item_id:
            workorder = item
    
    equipment_uuid = item["equipment"]

    equipment = Load_single_equipment_object(equipment_uuid)

    return equipment
    
    






