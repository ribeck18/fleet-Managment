from classes.Maintenance import MaintenanceItem

from datetime import datetime

from pathlib import Path

import json


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "maintenance_data.json"


def add_maintenance_item(title: str, info: str, due_date: datetime.date, equipment: str) -> MaintenanceItem:
    
    new_item = MaintenanceItem(title=title, info=info, due_date=due_date, equipment=equipment)

    m_list = load_maintenance_items()
    m_list.append(new_item.get_dict)
    return new_item 

def load_maintenance_items() -> list[dict]:
    """Returns DATA_PATH as a list of dictionaries."""
    try:
        with open(DATA_PATH, "r") as f:
            m_list = json.load(f)
            return m_list
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save_maintenance_list(data: list[dict]) -> None:
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4, default=str)

def load_single_maintenance_item(maintenance_id: str) -> MaintenanceItem:
    m_list = load_maintenance_items()
    for item in m_list:
        item_id = item.get("id")

        if item_id == maintenance_id:
            maintenance_item = item
            maintenance = MaintenanceItem.rehydrate(maintenance_item)
    return maintenance
    