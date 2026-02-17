import json
from pathlib import Path

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

def add_workorder(workorder: dict):
    """
    loads work orders as a list, appends work order to the list and dumps to the .json file.
    
    :param workorder: Description
    :type workorder: dict
    """
    workorders = load_workorders()
    workorders.append(workorder)
    save_workorder(workorders)






