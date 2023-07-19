#!/usr/bin/env python3
"""inserts based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts into school"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
