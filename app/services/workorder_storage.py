import json
from pathlib import Path
from classes.WorkOrders import WorkOrder

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






