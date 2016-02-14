import pymongo
import sys


# Copyright 2013, 10gen, Inc.
# Author: Andrew Erlichson


# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school                 # attach to db
collection = db.students         # specify the colllection

student_id = -1

# {"type": "homework"}).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)]

for doc in collection.find():
    min_score = min([score['score'] for score in doc['scores'] if score['type']=='homework'])
    collection.update({"_id": doc['_id']}, {'$pull': {"scores": {"score": min_score, 'type': 'homework'}}})
