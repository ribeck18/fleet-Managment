import uuid 

#Permission Levels: admin, mechanic, user

class User:
    def __init__(self, name, permission, company, email, password, username):
        self.name = name
        self.permission = permission
        self.company = company
        self.email = email
        self.password = password
        self.username = username
        self.id = str(uuid.uuid4())

    def get_dict(self):
        dictionary = {
            "name": self.name,
            "permission": self.permission,
            "company": self.company,
            "email": self.email,
            "password": self.password,
            "username": self.username,
            "id": self.id
        }
        return dictionary
    
    def get_string(self):
        string = f"{self.name}, {self.permission}, {self.company}, {self.email}, {self.password}, {self.username}, {self.id}"
        return string