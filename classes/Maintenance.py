from pydantic import field
from classes.Task import Task
from datetime import date


class Maintenance(Task):
    due_date: date
    due_miles: int
