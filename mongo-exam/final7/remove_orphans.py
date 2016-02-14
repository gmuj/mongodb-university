import pymongo

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.final7

albums = db.albums
images = db.images

for image in images.find():
    if not albums.find({'images': image['_id']}).count():
	images.remove({'_id': image['_id']}) 



