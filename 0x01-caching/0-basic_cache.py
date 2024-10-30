#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class with no limit on the cache size"""

    def put(self, key, item):
        """Assigns the item value to the key in self.cache_data."""

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to key in self.cache_data."""
        return self.cache_data.get(key, None)
