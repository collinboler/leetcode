class Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key: int, val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {} #key --> Node

        # dummy head/tail to avoid edge cases
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node) -> None:
        """Remove node from the doubly linked list."""
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
    
    def _add_to_front(self, node: Node) -> None:
        """Insert node right after head (mark as MRU)."""
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        # move to front (MRU)
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            # move to front (MRU)
            self._remove(node)
            self._add_to_front(node)
            return
        
        # new key
        node = Node(key, value)
        self.map[key] = node
        self._add_to_front(node)

        if len(self.map) > self.cap:
            # evict LRU (node before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)