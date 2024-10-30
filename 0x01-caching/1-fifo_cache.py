#!/usr/bin/env python3
"""FIFOCache module with FIFO eviction policy"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class with a FIFO eviction policy"""

    def __init__(self):
        """Initialize FIFOCache and order tracking"""
        super().__init__()
        self.order = []  # List to maintain the insertion order of cache keys

    def put(self, key, item):
        """Adds an item to the cache and applies FIFO eviction if needed"""
        if key is None or item is None:
            return  # Ignore None input

        # Check if eviction is needed
        if key not in self.cache_data and
        len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the oldest item (first in order list)
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        # Update the cache and maintain the order list
        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)  # Remove existing key to avoid duplicates
        self.order.append(key)  # Add key as the most recent entry

    def get(self, key):
        """Retrieves the item from cache by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
