class Soldier:
    def __init__(self, soldier_id, first_name, last_name, phone_number, rank):
        self.soldier_id = soldier_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    def __str__(self):
        return f"ID: {self.soldier_id}, Name: {self.first_name} {self.last_name}, Phone: {self.phone_number}, Rank: {self.rank}"