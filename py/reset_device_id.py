#!/usr/local/bin/python3
# encoding=utf-8

import sys
import argparse
from pymongo import MongoClient
from pymongo import database


mongo_db_uri_dev = "mongodb://hide"
mongo_db_uri_test = "mongodb://hide"

def parse_args():
    parser = argparse.ArgumentParser(description="delete user device id in test environment")
    parser.add_argument("-u", "--uid", required=True,
                        dest="uid", help="the user uid")
    opts = parser.parse_args()
    return opts

def init_mongodb():
    client = MongoClient(mongo_db_uri_test)
    db = client["dbname"]
    return db

def reset_device_id(db:database.Database, uid:str):
    hh_user = db.get_collection("user")
    user = hh_user.find_one({"userInfo.uid":uid})
    if user is None:
        print("user {} not found".format(uid))
        return

    device_id = user["userInfo"]["deviceID"]
    print("find user device id {}".format(device_id))

    result = hh_user.update_many({"userInfo.deviceID":device_id}, {"$set":{"userInfo.deviceID":""}})
    print(result)

if __name__ == "__main__":
    print(sys.argv)
    opts = parse_args()
    db = init_mongodb()
    reset_device_id(db, opts.uid)
