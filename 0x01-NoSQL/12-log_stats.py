#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs

    logs = db.nginx.count_documents({})
    get_count = db.nginx.count_documents({'method': 'GET'})
    post_count = db.nginx.count_documents({'method': 'POST'})
    put_count = db.nginx.count_documents({'method': 'PUT'})
    patch_count = db.nginx.count_documents({'method': 'PATCH'})
    delete_count = db.nginx.count_documents({'method': 'DELETE'})

    print("{} logs".format(logs))
    print("methods:")
    allcounts = {"GET": get_count, "POST": post_count, "PUT": put_count,
                 "PATCH": patch_count, "DELETE": delete_count}

    for key, value in allcounts.items():
        print("\tmethod {}: {}".format(key, value))

    status = db.nginx.count_documents({'method': 'GET', 'path': '/status'})
    print("{} status check".format(status))
