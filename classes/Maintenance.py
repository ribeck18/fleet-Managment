from pydantic import BaseModel, Field, ConfigDict, SkipValidation
from datetime import date
import uuid


class MaintenanceItem(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    title: str
    info: str
    due_date: date
    status: str = "Incomplete"
    id: uuid.uuid4 = Field(default_factory=uuid.uuid4)
    equipment: str  # This should be a uuid

    def get_dict(self):
        """Returns the object as a dictionary"""
        # This is a pydantic function that can quickly convert an object to a dictionary.
        return self.model_dump()

    def get_string(self):
        """Returns the objest as a string:

        title: info, due: due_date, status: status, equipment uuid: equipment_uuid
        """
        return f"{self.title}: {self.info}, due: {self.due_date}, status: {self.status}, equipment uuid: {self.equipment}"

    @classmethod
    def rehydrate(cls, data: dict):
        """Rehydrates from a dictionary back into an object, ensuring that it uses the same uuid it has already been assigned."""
        # This is a pydantic function that helps to quickly rehydrate an object from a dict.
        return cls.model_validate(data)

    def get_id(self):
        """Returns the uuid object of the maintenance object.

        Note: this is not in string format.
        """
        return self.id
