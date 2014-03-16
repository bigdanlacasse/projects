"""
    Docs: http://api.mongodb.org/python/current/tutorial.html
"""
from pymongo import MongoClient

class DB (object):
    """
    Wrapper for MongoClient - get connection to specified collection
    """
    def __init__(self, dbname="gw2", collect="meta"):
        self.client = MongoClient()
        self.db = self.client[dbname]
        self.collection = self.db[collect]
    
    
    def getCollection(self):
        return self.collection
    
    def getDB(self):
        return self.db
    
    """
        Wrapper for inserting a document into this collection
    """
    def insert(self, document=None):
        if document is not None:
            self.collection.insert(document)
        
    def save(self, document=None):
        if document is not None:
            self.collection.save(document)
            
    def findOne(self, query=None):
        return self.collection.find_one(query)

    def find(self, query=None):
        return self.collection.find(query)
    
    def find_list(self, query=None):
        results = []
        cursor = self.collection.find(query)
        for item in cursor:
            results.append(item)
        return results

    def drop_collection(self):
        return self.collection.drop()
    
    def map_reduce(self, mapFunction, reduceFunction, result_collection=None, query=None):
        return self.collection.map_reduce(mapFunction, reduceFunction, result_collection, query=query)
  
    