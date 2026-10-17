from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # self.version = {}
        self.map = {}
        self.cache = deque()
        
    def get(self, key: int) -> int:
        # return -1 or 1 update cache, get key
        if key not in self.map:
            return -1
        self.map[key] = (self.map[key][0], self.map[key][1] + 1)
        self.cache.append((key, self.map[key][1]))
        return self.map[key][0]

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            self.map[key] = (value, 1)
            self.cache.append((key, 1))
        else:
            self.map[key] = (value, self.map[key][1] + 1)
            self.cache.append((key, self.map[key][1]))
        
        while len(self.map) > self.capacity:
            k, v = self.cache.popleft()
            if v != self.map[k][1]:
                continue
            del self.map[k]
        
            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)