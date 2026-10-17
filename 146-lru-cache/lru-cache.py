from collections import deque
class LRUCache: 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.cache = deque()
        self.version = {}
 
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.version[key] += 1
        self.cache.append((key, self.version[key]))
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        # if not exist, add to map (val, version) and cache (key)
        if key not in self.map:
            self.map[key] = value 
            self.version[key] = 1
            self.cache.append((key, 1))
        else:
            # increment version
            self.map[key] = value
            self.version[key] += 1
            self.cache.append((key, self.version[key]))
            
        # add key-val to cache
        
        while len(self.map) > self.capacity:
            # if cache key's current version != cache key's version
            oldkey, oldversion = self.cache.popleft()
            if oldversion != self.version[oldkey]:
                continue # skip
            del self.map[oldkey] # two birds one stone again
    
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)