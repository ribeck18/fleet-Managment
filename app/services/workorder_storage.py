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

def save_workorder(workorders: list):
    """
    rewrites json file with the workorder list.

    :param workorders: updated workorder list
    :type workorders: list
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
            break
        
    return workorder

#Get the equipment item associated with the workorder.
def get_equipment(workorder_id):
    """
        This function loads the equipment item that is associated with the workorder.
    """
    workorder_list = load_workorders()

    # Finds the uuid for each workorder in the list, so that it can be compared to the workorder UUID argument.
    for item in workorder_list:
        item_id = item["id"]

        #Set workorder to the current item in the loop so that equip UUID can be accessed. 
        if workorder_id == item_id:
            workorder = item
    
    equipment_uuid = workorder["equipment"] # The bug was because item was here instead of workorder.

    equipment = Load_single_equipment_object(equipment_uuid)

    return equipment
    

def update_workorder(workorder_id: str):
    workorder = get_single_workorder(workorder_id)




#Note this won't edit, it will just create a new one with the same uuid.
def resolve(workorder_id: str):
    """
    Finds a specific workorder, and changes its severity level to resolved.
    The workorder list is then updated with the now updated workorder.
    The updated workorder list is saved to the json file.

    :param workorder_id: UUID of the workorder to resolve
    :type workorder_id: str
    """
    # Load workorders as a list
    my_list = load_workorders()
    # Find the correct work order and its index in the my_list variable
    for i, w in enumerate(my_list):
        w_id = w["id"]

        if w_id == workorder_id:
            workorder = w
            list_index = i
    # Edit the workorder item severity to resolved
    workorder["severity"] = "resolved"
    #Replace the index in the list with the updated workorder.
    my_list[i] = workorder

    save_workorder(my_list)

    return workorder


            



    








