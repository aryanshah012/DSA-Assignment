class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}  
        self.head = Node(0, 0)  
        self.tail = Node(0, 0) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove node from linked list."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _insert(self, node: Node):
        """Insert node right after head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
            self.size -= 1
        elif self.size == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
            self.size -= 1

        new_node = Node(key, value)
        self._insert(new_node)
        self.cache[key] = new_node
        self.size += 1

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  
lru.put(3, 3)      
print(lru.get(2))  
lru.put(4, 4)      
print(lru.get(1))  
print(lru.get(3))  
print(lru.get(4))  
