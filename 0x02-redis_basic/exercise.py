#!/usr/bin/env python3
"""Class cache"""
import uuid
import redis


class Cache:
    """class cache which contains an instance of redis"""
    def __init__(self):
        """class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> uuid.uuid4():
        """takes a data argument and returns a string.
        generates a random key (e.g. using uuid),
        stores the input data in Redis
        using the random key and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
