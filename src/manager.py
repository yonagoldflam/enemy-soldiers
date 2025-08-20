from soldier import Soldier
from dal import Dal

class Manager:
    def __init__(self):
        self.current_soldier = None
        self.dal = Dal()

    def get_all_data(self):
        return self.dal.get_all_data()

    def insert_soldier(self, soldier_dict):
        self.soldier_object_from_soldier_dict(soldier_dict)
        self.dal.insert_soldier(self.current_soldier)

    def update_soldier(self, field, value):
        self.dal.update_soldier(self.current_soldier, field, value)

    def delete_soldier(self):
        self.dal.delete_soldier(self.current_soldier)


    def soldier_object_from_soldier_dict(self,soldier_dict):
        self.current_soldier = Soldier(soldier_dict['soldier_id'], soldier_dict['first_name'], soldier_dict['last_name'], soldier_dict['phone_number'], soldier_dict['rank'])

    def update_current_soldier_by_id(self,soldier_id):
        soldier_dict = self.dal.get_soldier_by_id(soldier_id)
        self.soldier_object_from_soldier_dict(soldier_dict)







