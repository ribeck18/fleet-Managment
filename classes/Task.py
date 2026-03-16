from pydantic import BaseModel, Field
import uuid
from datetime import date


class Task(BaseModel):
    title: str
    description: str
    equipment: uuid.UUID
    created_date: date = Field(default_factory=date.today())
    self_id: uuid.UUID = Field(default_factory=uuid.uuid4)

    def get_dict(self) -> dict:
        """Get the object as a dict

        Returns:
            _type_: dict
        """
        return self.model_dump()

    @classmethod
    def rehydrate(cls, payload: dict) -> "Task":
        """
            Rehydrate an object from a dictionary format. Ensures that UUID remains the same so that duplicate items are not created.

        Args:
            payload (dict): dictionary of data to convert ton object.

        Returns:
            Equipment: Equipment object.
        """
        return cls.model_validate(payload)

    def get_string(self) -> str:
        """returns the object in string format.

        Returns:
            str: "NAME, MODEL, YEAR: STATUS"
        """
        return f"{self.name}, {self.model}, {self.year}: {self.status}"

    def get_id(self) -> uuid.UUID:
        """Gets the uuid of the object.

        Returns:
            uuid.UUID
        """
        return self.id
