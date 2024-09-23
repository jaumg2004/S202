from pymongo import MongoClient

class Database:
    def __init__(self, uri="mongodb://localhost:27017/"):
        self.client = MongoClient(uri)
        self.db = self.client['Motoristas']

    def get_motoristas_collection(self):
        return self.db['Motoristas']
