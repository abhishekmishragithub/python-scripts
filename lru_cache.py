# TODO: Add the method to get cache hit, miss, and other info

from collections import OrderedDict


class LRUCache:
    """
    A class representing a Least Recently Used (LRU) Cache.

    Attributes:
        cache (OrderedDict): The cache to store key-value pairs.
        capacity (int): The maximum number of key-value pairs the cache can hold.

    Methods:
        get(key: int) -> int:
            Retrieves the value associated with the given key from the cache.
            Returns -1 if the key is not present in the cache.

        put(key: int, value: int) -> None:
            Inserts or updates the value associated with the given key in the cache.
            If the cache is already at capacity, the least recently used item is evicted.
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Indicates that the key is not present
        else:
            # Move the key to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move the key to the end because it will be the most recently used
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Pop the first item if we're at capacity
            self.cache.popitem(last=False)
        self.cache[key] = value


cache = LRUCache(2)  # capacity of 2
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))   # returns 1
cache.put(3, 3)       # evicts key 2
print(cache.get(2))   # returns -1 (not found)
cache.put(4, 4)       # evicts key 1
print(cache.get(1))   # returns -1 (not found)
print(cache.get(3))   # returns 3
print(cache.get(4))   # returns 4
