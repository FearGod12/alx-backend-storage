#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs

    print("{} logs".format(db.nginx.count_documents({})))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method,
                                       db.nginx.count_documents
                                       ({"method": method})))
    print("{} status check".format(db.nginx.count_documents({
                                   "method": "GET", "path": "/status"})))
