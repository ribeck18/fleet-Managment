from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import equipment, workorder, html

from pathlib import Path


##To Do
#When a work order is saved the entered equipment uuid is not shown in the table. note: it is saved in the json file.
#Clean up the html
#add css
#when a workorder is created add a dropdown menu to select an equipment item. 

app = FastAPI()


#Mount the static files to the app. 
app.mount("/static", StaticFiles(directory="static"), name="static")

#Include all routers
app.include_router(html.router)
app.include_router(equipment.router)
app.include_router(workorder.router)