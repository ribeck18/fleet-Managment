import uuid

class Equipment:

    def __init__(self, name, year, status, notes=""):
        self.name = name
        self.year = year
        self.status = status
        self.notes = notes
        self.id = uuid.uuid4()
        
    
    def get_string(self):
        """
        Return the equipment object as a string

        :return: equipment object in string form
        """
        return f"{self.name}, {self.info}, {self.id}"
    
    def get_json(self):
        """
        returns the equipment object as a string
        
        :return: equipment object in dictionary form
        """
        return self.__dict__
    