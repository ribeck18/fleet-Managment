import uuid

class Equipment:

    def __init__(self, name, info):
        self.name = name 
        self.info = info
        
        equipid = uuid.uuid4()
        self.id = str(equipid)
        
    def get_equipment(self):
        return f"{self.name}, {self.info}, {self.id}"
    
    def get_json(self):
        equip_dict = {
            "name": self.name,
            "info" : self.info,
            "uuid" : self.id
        }
        return equip_dict
    