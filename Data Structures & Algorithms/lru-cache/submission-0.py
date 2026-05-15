class DLLNode:
    def __init__(self, prev=None, nxt=None, key=None, val=None):
        self.prev = prev
        self.nxt = nxt
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.lru_map = {}
        self.capacity = capacity
        self.dll_head = DLLNode()
        self.dll_tail = DLLNode()
        self.dll_head.nxt = self.dll_tail
        self.dll_tail.prev = self.dll_head

    def get(self, key: int) -> int:
        if key in self.lru_map:
            n = self.lru_map[key]
            self.remove_links(n)
            self.move_to_head(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_map:
            n = self.lru_map.pop(key)
            self.remove_links(n)
        n = DLLNode(key=key, val=value)
        self.lru_map[key] = n
        self.move_to_head(n)
        if len(self.lru_map) > self.capacity:
            lru = self.dll_tail.prev
            del self.lru_map[lru.key]
            self.remove_links(lru)
        
    def remove_links(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
    
    def move_to_head(self, node):
        prev_head = self.dll_head.nxt
        prev_head.prev = node
        node.nxt = prev_head
        node.prev = self.dll_head
        self.dll_head.nxt = node