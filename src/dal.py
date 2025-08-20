from db_connection import Connection
from pymongo.errors import PyMongoError
from soldier import Soldier


class Dal:
    def __init__(self):
        self.connection = Connection()


    def get_all_data(self):
        try:
            collection = self.connection.db[self.connection.collection_name]
            return list(collection.find({}, {"_id": 0}))
        except PyMongoError as e:
            print(f"Error reading data: {e}")
            return []

    def get_soldier_by_id(self,soldier_id):
        try:
            collection = self.connection.db[self.connection.collection_name]
            return list(collection.find_one({"_id": soldier_id}))
        except PyMongoError as e:
            print(f"Error reading data: {e}")
            return []

    def insert_soldier(self, soldier: Soldier):
        try:
            collection = self.connection.db[self.connection.collection_name]
            result = collection.insert_one(soldier.__dict__)
            return {f"successfully: {str(result.inserted_id)}"}
        except PyMongoError as e:
            return f"Error inserting soldier: {e}"

    def update_soldier(self, soldier: Soldier, field: str, value):
        try:
            collection = self.connection.db[self.connection.collection_name]
            result = collection.update_one(
                {"soldier_id": soldier.soldier_id},
                {"$set": {field: value}}
            )
            return {f"successfully: {str(result.inserted_id)}"}
        except PyMongoError as e:
            return f"Error inserting soldier: {e}"

    def delete_soldier(self, soldier: Soldier):
        try:
            collection = self.connection.db[self.connection.collection_name]
            result = collection.delete_one({"soldier_id": soldier.soldier_id})
            return {f"successfully: {str(result.inserted_id)}"}
        except PyMongoError as e:
            return f"Error deleting soldier: {e}"




