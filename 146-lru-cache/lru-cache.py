from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.version = {}
        self.map = {}
        self.cache = deque()
        
    def get(self, key: int) -> int:
        # return -1 or 1 update cache, get key
        if key not in self.map:
            return -1
        self.version[key] += 1
        self.cache.append((key, self.version[key]))
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            self.version[key] = 1
            self.map[key] = value
            self.cache.append((key, 1))
        else:
            self.version[key] += 1
            self.map[key] = value
            self.cache.append((key, self.version[key]))
        
        while len(self.map) > self.capacity:
            k, v = self.cache.popleft()
            if v != self.version[k]:
                continue
            del self.map[k]
            del self.version[k]
        
            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)