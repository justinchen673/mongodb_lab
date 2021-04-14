import pprint
from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient()

def fetchAll(collection):
    for doc in collection.find():
        pprint.pprint(doc)

def fetchOne(collection):
    pprint.pprint(collection.find_one())

def fetchSpecific(key, value, collection):
    pprint.pprint(collection.find_one({key: value}))

def fetchById(id, collection):
    pprint.pprint(collection.find_one({"_id": ObjectId(id)}))

def insertRecord(query, collection):
    pprint.pprint(collection.insert_one(query))

if __name__ == '__main__':
    db = client["mongo_db_lab"]
    defs = db["definitions"]
    #fetchAll(defs)
    #fetchOne(defs)
    #fetchById("56fe9e22bad6b23cde07b949", defs)
    #insertRecord({"word": "Bubly", "definition": "Greatest sparkling water"}, defs)
    #fetchSpecific("word", "Bubly", defs)
