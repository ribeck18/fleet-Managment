import uuid

class Equipment:

    def __init__(self, name, year, status, notes=""):
        self.name = name
        self.year = year
        self.status = status
        self.notes = notes
        self.id = str(uuid.uuid4())
        
    
    def get_string(self):
        """
        Return the equipment object as a string

        :return: equipment object in string form
        """
        return f"{self.name}, {self.year}, {self.status}, {self.notes}, {self.id}"
    
    def get_dict(self):
        """
        returns the equipment object as a dictioanry
        
        :return: equipment object in dictionary form
        """
        equipment_dict = {
            "name": self.name,
            "year": self.year,
            "status": self.status,
            "notes": self.notes,
            "id": self.id
        }
        return equipment_dict
    