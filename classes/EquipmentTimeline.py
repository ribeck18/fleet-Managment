from pydantic import BaseModel
from classes.WorkOrders import WorkOrder
from classes.Maintenance import MaintenanceItem


class EquipmentTimeline:

    equipment: str
    workorders: list[WorkOrder]
    maintenance_list: list[MaintenanceItem]

    # This should assemble an array of the equipment items history.
    def assemble_timeline(self):
        timeline = []
        workorderdates = []
        for workorder in self.workorders:
            date = workorder.get_date()

    # Display the timeline
    def get_timeline():
        pass

    def get_equipment_uuid():
        pass
