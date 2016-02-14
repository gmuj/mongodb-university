import pymongo
import sys


# Copyright 2013, 10gen, Inc.
# Author: Andrew Erlichson


# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students                 # attach to db
collection = db.grades         # specify the colllection

student_id = -1

for doc in collection.find({"type": "homework"}).sort([("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)]):
    print doc
    if doc['student_id'] != student_id:
        student_id = doc['student_id']
	print "Removing: %s" % doc["_id"]
        collection.remove({"_id": doc["_id"]})
