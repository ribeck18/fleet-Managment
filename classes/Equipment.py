import uuid

class Equipment:

    #Initallize a new object
    def __init__(self, name, year, status, notes="", id=None):
        self.name = name
        self.year = year
        self.status = status
        self.notes = notes
        self.id = id or str(uuid.uuid4())


    #Rehydrate an object from json
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name = data["name"],
            year = data["year"],
            status = data["status"],
            notes = data["notes"],
            id = data["id"]
        )
        
    
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
    
    def get_id(self):
        return self.id
    
    