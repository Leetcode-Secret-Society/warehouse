import time
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque()
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            now = time.time()
            self.queue.append((key, now))
            self.cache[key] = (self.cache[key][0], now)
            return self.cache[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        now = time.time()
        self.cache[key] = (value, now)
        self.queue.append((key, now))
        while len(self.cache) > self.capacity:
            expired_key, expired_time = self.queue.popleft()
            if self.cache[expired_key][1] == expired_time:
                del self.cache[expired_key]
