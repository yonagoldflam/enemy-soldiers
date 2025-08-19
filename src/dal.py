from db_connection import Connection
from pymongo.errors import PyMongoError

class Dal:
    def __init__(self):
        self.connection = Connection()

    def get_data(self):
        try:
            collection = self.connection.db[self.connection.collection_name]
            return list(collection.find({}, {"_id": 0}))
        except PyMongoError as e:
            print(f"Error reading data: {e}")
            return []

    # def update(self,soldier_id,):
    #
    #