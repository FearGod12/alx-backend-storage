#!/usr/bin/env python3
"""Function that lists all documents in a collection in mongo db"""


def list_all(mongo_collection):
    """list all in a collection"""
    result = mongo_collection.find()
    if not result:
        return []
    return result
