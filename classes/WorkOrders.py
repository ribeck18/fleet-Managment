import uuid
from datetime import datetime

class WorkOrder():

    def __init__(self, title, info, user, severity, equipment):
        self.title = title
        self.info = info 
        self.user = user
        self.severity = severity
        self.equipment = equipment
        self.date = str(datetime.now())
        self.id = str(uuid.uuid4())

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title = data.get("title"),
            info = data.get("info"),
            user = data.get("user"),
            severity = data.get("severity"),
            equipment = data.get("equipment"),
            date = data.get("date"),
            id = data.get("id")
        )
    
    def get_string(self):
        """
        return work order as a string
        
        :return: string
        """
        return f"{self.title}, {self.info}, {self.user}, {self.severity}, {self.equipment_id}, {self.date}, {self.id}"

    def get_dict(self):
        """
        return work order as a dictionary
        
        :return: dict
        """
        return self.__dict__
    
    def get_equip(self):
        """
        Returns the equipment item id associated with the class

        :return: equipment uuid
        """
        return self.equipment    

