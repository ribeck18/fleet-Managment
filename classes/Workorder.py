from classes.Task import Task
from pydantic import Field
import uuid


class Workorder(Task):
    severity: str = Field(defualt_factory="low")
    user: uuid.UUID
