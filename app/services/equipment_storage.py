import json
from classes.Equipment import Equipment

from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "equipment_data.json"

def load_equipment():
    """
    Reads the equipment storage file 

    :returns: List equipment dictionaries
    """
    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    return data

def save_equipment(data):
    with open(DATA_PATH , "w") as f: 
        json.dump(data, f, indent=4, default=str)
    

def create_equipment(name, year, status, notes):
    equipment = Equipment(name, year, status, notes)
    data = load_equipment()
    data.append(equipment.get_dict())
    save_equipment(data)

    return equipment.get_string()

def load_single_equipment(choice: str):
    """
    Loops over all equipment items and checks if user choice matches the equipment. Return the equipment that matches.
    
    :param choice: uuid of equipment item you would like to display.
    :type choice: str

    :return: returns a single equipment item as a dictionary.
    """
    equipment_list = load_equipment()
    equipment ={}
    #Loop over all equipment and check if equip uuid == choice Store chosen equipment in equipment var
    for i in equipment_list:
        equip_id = i["id"]

        if equip_id == choice:
            equipment = i

    #If no matching equipment is founnd.
    if equipment == {}:
        return "No equipment found."
    
    return equipment
