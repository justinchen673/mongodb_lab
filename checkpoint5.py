import datetime
from random import randrange
import pprint
from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient()

def random_word_requester():
    # Connection to db
    db = client["mongo_db_lab"]
    collection = db["definitions"]

    # Get random document
    randIndex = randrange(collection.count_documents({}))
    count = 0
    for doc in collection.find():
        if (randIndex == count):
            # Add date to the document
            dt = datetime.datetime.isoformat(datetime.datetime.utcnow())
            if ("dates" not in doc):
                doc["dates"] = []
            doc["dates"].append(dt)
            collection.update_one({"word": doc["word"]}, {"$set": doc})

            return doc

        count += 1

if __name__ == '__main__':
    pprint.pprint(random_word_requester())
