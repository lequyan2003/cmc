import requests
import pymongo
import config
import pprint


def getData():
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config.API_KEY["api-key"]
    }

    parameters1 = {
        "listing_status": "active",
        "start": 1,
        "limit": 300,
        "sort": "cmc_rank"
    }

    parameters2 = {
        "start": 1,
        "limit": 300
    }

    try:
        info1 = requests.get(config.url["cmc_id_map_url"], params=parameters1, headers=headers).json()
        if info1['status']['error_code'] != 0:
            print(info1['status']['error_code'])
            return None
        info2 = requests.get(config.url["listings_latest_url"], params=parameters2, headers=headers).json()
        if info2['status']['error_code'] != 0:
            print(info2['status']['error_code'])
            return None
    except IndexError:
        print("IndexError occurred")

    tmp1 = {}
    for i in range(len(info1["data"])):
        tmp1.update({info1["data"][i]["name"]: [info1["data"][i]]})

    tmp2 = {}
    for i in range(len(info2["data"])):
        tmp2.update({info2["data"][i]["name"]: info2["data"][i]})

    for coin in tmp1:
        if coin in tmp2:
            tmp1[coin].append(tmp2[coin])

    return tmp1

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Cryptocurrencies"]
mycol = mydb["data"]

mydb["data"].drop()
rec = getData() 
mycol.insert_one(rec)



