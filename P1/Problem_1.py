class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._set_head(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        if self.capacity == 0:
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self._remove_node(self.cache[key])
            new_node = Node(value)
            self.cache[key] = new_node
            self._set_head(new_node)
        else:
            if self.size == self.capacity:
                self._remove_LRU()
            new_node = Node(value)
            self.cache[key] = new_node
            self._set_head(new_node)
            self.size += 1
            
    def _set_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            
    def _remove_node(self, node):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head.next.prev = None
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
                
    def _remove_LRU(self):
        node = self.tail
        del self.cache[node.value]
        self._remove_node(node)
        self.size -= 1



# Tests 

our_cache = LRU_Cache(4)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(4))     # returns 4
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(4, 5)
print(our_cache.get(4))     # return 5 because it is updated

our_cache.set(6, 6)
print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entr