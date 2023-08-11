import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol=mydb["good"]

#print(myclient.list_collection_name())
print(mydb.list_collection_names())