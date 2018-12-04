import pymongo

class DataBase:

    collection = None

    def __init__(self):
        self.connection = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.connection["escola"]
        self.collection = self.database["aluno"]

    def getCollection(self):
        return self.collection
