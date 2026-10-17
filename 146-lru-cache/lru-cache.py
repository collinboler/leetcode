from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # key -> (value, version)
        self.cache = deque()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        value, version = self.map[key]
        version += 1

        self.map[key] = (value, version)
        self.cache.append((key, version))

        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            version = 1
        else:
            version = self.map[key][1] + 1

        self.map[key] = (value, version)
        self.cache.append((key, version))

        while len(self.map) > self.capacity:
            oldkey, oldversion = self.cache.popleft()

            if oldversion != self.map[oldkey][1]:
                continue

            del self.map[oldkey]