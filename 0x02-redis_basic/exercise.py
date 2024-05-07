#!/usr/bin/env python3
"""Cache class the uses redis"""

import redis
from typing import Union, Callable
import uuid


class Cache:
    """Cache class"""
    def __init__(self) -> None:
        """Initialization of Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, int, str, float]) -> str:
        """Generate random key and stores it in redis.
        Arg:
            - data: Any data. It could be int, float, string.
        Return:
            key: Key to the stored data.
        """
        # Generate random UUID key
        key = str(uuid.uuid4())

        # Store the data with the key
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None)\
            -> Union[int, str, bytes, float]:
        """Convert data from redis to python equivalent
        Args:
            - key (str): The key to search for value in redis.
            - fn (Callable=None): To covert data to python equivalent.
        Return:
            Data: Converted value from redis server.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Converts values from redis to string.
        Arg:
            - key (str): The key to fetch data from redis.
        Return:
            Converted data"""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Convert Values from redis
        Arg:
            - key (str): The key to fetch data from redis.
        Return:
            Converted data.
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
