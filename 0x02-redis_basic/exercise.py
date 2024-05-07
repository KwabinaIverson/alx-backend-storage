#!/usr/bin/env python3
"""Cache class the uses redis"""

import redis
from typing import Union
import uuid


class Cache:
    """Cache class"""
    def __init__(self):
        """Initialization of Cache class"""
        self._redis = redis.Redis(host='127.0.0.1',
            port=6379, db=0, decode_responses=True)
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
