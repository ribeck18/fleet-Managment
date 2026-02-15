import uuid
from datetime import datetime

class WorkOrder():

    def __init__(self, title, info, user, severity, equipment):
        self.title = title
        self.info = info 
        self.user = user
        self.severity = severity
        self.equipment_id = equipment
        self.date = datetime.now()
        self.id = uuid.uuid4()
    
    def get_work_order_string(self):
        """
        return work order as a string
        
        :return: string
        """
        return f"{self.title}, {self.info}, {self.user}, {self.severity}, {self.equipment_id}, {self.date}, {self.id}"

    def get_work_order_dict(self):
        """
        return work order as a dictionary
        
        :return: dict
        """
        return self.__dict__
    
    
