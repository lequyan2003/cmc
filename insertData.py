from pymongo import MongoClient
from getData import *
# from getMetaData import *
import config

try:
    client = MongoClient(config.mongodb["mongodb_url"])
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = client[config.mongodb["myDataBase"]]
collection = db[config.mongodb["myCollection"]]

rec = getData()
# rec = getMetaData()
rec["_id"] = 0

collection.insert_one(rec)
