#!/usr/bin/env python3
"""Class cache"""
import uuid
from typing import Union, Callable, Optional
from functools import wraps

import redis


def count_calls(method: Callable) -> Callable:
    """count decorator"""
    key = method.__qualname__

    @wraps(method)
    def increment(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(key)
        return method(self, *args, *kwargs)

    return increment


def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs"""
    key1 = method.__qualname__ + ":inputs"
    key2 = method.__qualname__ + ":outputs"

    @wraps(method)
    def history(self, *args, **kwargs):
        """stores the history of inputs and outputs"""
        self._redis.rpush(key1, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(key2, data)
        return data

    return history


class Cache:
    """class cache which contains an instance of redis"""

    def __init__(self) -> None:
        """class constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[int, float, bytes, str]) -> str:
        """takes a data argument and returns a string.
        generates a random key (e.g. using uuid),
        stores the input data in Redis
        using the random key and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, float, int, bytes, None]:
        """take a key string argument and an optional Callable argument
        named fn. This callable will be used to convert the data back to
        the desired format."""
        value = self._redis.get(key)
        if value is not None:
            if fn is not None:
                return fn(value)
            return value
        return value

    def get_str(self, value: bytes) -> str:
        """converts to string"""
        return value.decode("utf-8")

    def get_int(self, value: bytes) -> int:
        """converts to int from bytes"""
        return int.from_bytes(value)


def replay(method: Callable) -> None:
    """display the number of times a particular function was called"""
    key1 = method.__qualname__ + ":inputs"
    key2 = method.__qualname__ + ":outputs"
    redis = method.__self__._redis
    inputs = redis.lrange(key1, 0, -1)
    outputs = redis.lrange(key2, 0, -1)

    print("{} was called {} times".format(method.__qualname__, len(inputs)))
    for args, output in zip(inputs, outputs):
        args, output = eval(args), output.decode("utf-8")
        print("{}(*{}) -> {}".format(method.__qualname__, tuple(args), output))
