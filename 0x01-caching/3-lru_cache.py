#!/usr/bin/env python3
"""implement an LRU (Least Recently Used) Cache"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU Caching System"""

    def __init__(self):
        """Initialize the class with the parent's attributes"""
        super().__init__()
        self.cache_data = OrderedDict()  # Use OrderedDict  track access order

    def put(self, key, item):
        """Add an item in the cache using the LRU policy"""
        if key is None or item is None:
            return

        # Update item if key exists or add a new item
        if key in self.cache_data:
            self.cache_data.move_to_end(key)  # Make it the most recently used
        self.cache_data[key] = item

        # Check if cache size exceeds MAX_ITEMS
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item (least recently used)
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Get an item by key and mark it as recently used"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)  # Move key to end to mark recent
            return self.cache_data[key]
        return None
