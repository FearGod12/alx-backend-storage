#!/usr/bin/env python3
"""simulates web cache tracker"""
import requests
import redis
from typing import Callable
from functools import wraps

client = redis.Redis()


def cache_content(method: Callable) -> Callable:
    """caches the content"""

    @wraps(method)
    def wrapper(url):
        """caches the content"""
        content = client.get(url)
        if content:
            return content.decode("utf-8")
        content = method(url)
        client.setex(url, 10, content)
        return content

    return wrapper


def tracker_time(method: Callable) -> Callable:
    """keeps track"""

    @wraps(method)
    def wrapper(url):
        """sets the number of times"""
        key = "count:{}".format(url)
        client.incr(key)
        return method(url)

    return wrapper


@cache_content
@tracker_time
def get_page(url: str) -> str:
    """makes a request to a page and tracks how many times it was done"""

    r = requests.get(url)
    content = r.text
    return content
