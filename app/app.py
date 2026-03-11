from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import (
    api_equipment,
    api_user,
    api_workorder,
    html_main,
    html_equipment,
    html_workorder,
    api_maintenance,
)

from pathlib import Path

##To Do
# Add functionality to edit equipment items
# Add functionality to resolve workorders
# Add functionality to open a workorder detail window
# Add user log in features
# Add a maintenance tracker

app = FastAPI()


# Mount the static files to the app.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include all routers
app.include_router(html_main.router)
app.include_router(api_equipment.router)
app.include_router(api_workorder.router)
app.include_router(api_user.router)
app.include_router(html_equipment.router)
app.include_router(html_workorder.router)
app.include_router(html_workorder.router)
app.include_router(api_maintenance.router)
