#!/usr/bin/enc python3
""" implement the LIFOCache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching System"""

    def __init__(self):
        """Initialize the class with the parent's attributes"""
        super().__init__()
        self.last_key = None  # Track the last key inserted

    def put(self, key, item):
        """Add an item in the cache using the LIFO policy"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key:
                    # Discard the last added item (LIFO)
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
            # Update the last key after any insertion
            self.last_key = key

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
