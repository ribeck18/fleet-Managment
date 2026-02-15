from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import json
from pathlib import Path

from classes.Equipment import Equipment



app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

DATA_PATH = Path(__file__).resolve().parent / "data.json"

#Create an item and append it to the JSON file
@app.post("/add-equipment")
def create_equipment(name: str=Form(""), year: str=Form(""), status: str=Form("")):
    """
    Asks the user for a name, year, and status in order to create a new equipment item.
    Opens a file under DATA_PATH and loads the json already there. It then appends the new equipment dictionary to the list of dictionaries and rewrites the json file with the newly appended list.

    :param name: Name of equipment item
    :type name: str
    :param year: Year that the equipment was built
    :type year: str
    :param status: current status of the equipment item
    :type status: str
    
    :returns: The path of the save file, and the equipment saved. 
    """

    equipment = Equipment(name, year, status)

    try:
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(equipment.get_json())

    with open(DATA_PATH , "w") as f: 
        json.dump(data, f, indent=4)
    
    return {"Saved to": str(DATA_PATH), "equipment": equipment.get_string()}

#Return a feed of all the equip items
@app.get("/view-equipment")
def get_equipment():
    """
    Opens the file under DATA_PATH and reads the contents of the file

    :returns: all of the equipment from the equipment file.
    """
    try:
        with open (DATA_PATH, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    
    return {"Equipment": data}

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    """
    get and return the HTML for the home page
    
    :returns: HTML from home.jinja2
    """
    return templates.TemplateResponse(
        "home.jinja2",
        {'request': request}
    )
    