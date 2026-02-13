from fastapi import FastAPI, Form
from classes.Equipment import Equipment
import json
from pathlib import Path


app = FastAPI()

DATA_PATH = Path(__file__).resolve().parent / "data.json"

#Create an item and append it to the JSON file
@app.post("/add-equipment")
def create_equipment(name: str=Form(""), info: str=Form("")):

    equipment = Equipment(name, info)

    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(equipment.get_json())

    with open(DATA_PATH , "w") as f: 
        json.dump(data, f, indent=4)
    
    return {"Saved to": str(DATA_PATH), "equipment": equipment.get_equipment()}

#Return a feed of all the equip items
@app.get("/view-equipment")
def get_equipment():

    try:
        with open (DATA_PATH, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    return {"Equipment": data}
    