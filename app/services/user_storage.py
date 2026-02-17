from classes.User import User
from pathlib import Path
import json

DATA_PATH = Path(__file__).resolve().parent.parent /"data"/"user_data.json"

def load_users():
    """
    Loads all users from '/app/data/user_data.json' as a list of dictionaries.

    :returns: List of user dictionaries
    """
    with open(DATA_PATH, "r") as f:
        try:
            data = json.load(f)
        except(FileExistsError, json.JSONDecodeError):
            data = []
    return data

def save_users(users):
    with open(DATA_PATH, "w") as f:
        json.dump(users, f, indent=4, default=str)

def create_user(name: str, permission: str, company: str, email: str, password:str , username: str):
    """
    creates a new user object, loads all users from '/app/data/user_data.json' as a list, then appends the new user object to the list.
    updated list is dumped back to the json file.
    
    :param name: new user's name
    :type name: str
    :param permission: permission level: "admin", "mechanic", "user"
    :type permission: str
    :param company: Company Name
    :type company: str
    :param email: user email
    :type email: str
    :param password: user password
    :type password: str
    :param username: user username.
    :type username: str

    :returns: new user as dictionary
    """
    user = User(name, permission, company, email, password, username)

    data = load_users()
    data.append(user.get_dict())
    save_users(data)

    return user.get_dict()
    

def delete_user():
    pass

def edit_user():
    pass
