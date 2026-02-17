from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import equipment, workorder, html

from pathlib import Path


##To Do
#Finish work order routes and services
#Connect routes to app
#Connect HTML Routes to app

app = FastAPI()


#Mount the static files to the app. 
app.mount("/static", StaticFiles(directory="static"), name="static")

#Include all routers
app.include_router(html.router)
app.include_router(equipment.router)
app.include_router(workorder.router)