from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import equipment, workorder, html, user

from pathlib import Path

##To Do
#Add functionality to edit equipment items
#Add functionality to resolve workorders
#Add functionality to open a workorder detail window
#Add user log in features
#Add a maintenance tracker

app = FastAPI()


#Mount the static files to the app. 
app.mount("/static", StaticFiles(directory="static"), name="static")

#Include all routers
app.include_router(html.router)
app.include_router(equipment.router)
app.include_router(workorder.router)
app.include_router(user.router)