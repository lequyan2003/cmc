from pymongo import MongoClient
from main import *
import config

try:
    cluster = MongoClient(config.mongodb["mongodb_url"])
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

db = cluster[config.mongodb["myDataBase"]]
collection = db[config.mongodb["myCollection"]]

rec = getInfo()

collection.insert_one(rec)
