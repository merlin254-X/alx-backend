#!/usr/bin/env python3
""" implement an MRU (Most Recently Used) Cache """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU Caching System"""

    def __init__(self):
        """Initialize the class with the parent's attributes"""
        super().__init__()
        self.cache_data = OrderedDict()  # use to maintain insertion order

    def put(self, key, item):
        """Add an item in the cache using the MRU policy"""
        if key is None or item is None:
            return

        # Update or add item
        if key in self.cache_data:
            self.cache_data.move_to_end(key)  # Mark as recently used

        self.cache_data[key] = item

        # If cache size exceeds MAX_ITEMS, discard the most recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key, _ = self.cache_data.popitem(last=True)  # Remove the last
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """Get an item by key and mark it as recently used"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)  # Mark key as recently used
            return self.cache_data[key]
        return None
