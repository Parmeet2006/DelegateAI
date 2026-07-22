from pymongo import MongoClient
from pymongo.server_api import ServerApi
from config import MONGODB_URI

class DBHelper():
    def __init__(self,db_name="TR2026"):
        self.client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
        self.db=self.client[db_name]
        print('[DBHelper] Connection Created')

    def select_collection(self, collection_name='Users'):
        self.collection=self.db[collection_name]
        print('[DBHelper] selected collection:',collection_name)
    
    def save(self,document):
        insert_id=self.collection.insert_one(document)
        print("[DBHelper] Document Saved. Id is:",insert_id)

    def retrieve(self):
        result=self.collection.find()
        print("[DBHelper] Document retrieved. Id is:",result)

        for document in result:
            print(document)
        
        

