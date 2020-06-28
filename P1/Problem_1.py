class Node:
    def __init__(self, key, value):
        self.key = key
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
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._set_head(new_node)
        else:
            if self.size == self.capacity:
                self._remove_LRU()
            new_node = Node(key, value)
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
        del self.cache[node.key]
        self._remove_node(node)
        self.size -= 1


# test case 1
print("test case 1")
our_cache = LRU_Cache(4)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))     # 1
print(our_cache.get(2))     # 2
print(our_cache.get(4))     # 4
print(our_cache.get(9))     # -1
our_cache.set(4, 5)
print(our_cache.get(4))     # 5
print(our_cache.get(3))     # 3

# test case 2
print("test case 2")
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(4))  # 4
print(our_cache.get(1))  # -1
our_cache.set(2, 4)
print(our_cache.get(2))  # 4
our_cache.set(5, 5)
print(our_cache.get(3))  # -1
print(our_cache.get(5))  # 5
our_cache.set(2, 6)
print(our_cache.get(2))  # 6
our_cache.set(6, 6)
print(our_cache.get(4))  # -1
print(our_cache.get(6))  # 6
our_cache.set(5, 10)
our_cache.set(7, 7)
print(our_cache.get(2))  # -1

# test case 3
print("test case 3")
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
our_cache.set(2, 4)
our_cache.set(3, 5)
print(our_cache.get(2))  # -1
print(our_cache.get(1))  # -1
print(our_cache.get(5))  # -1
print(our_cache.get(3))  # -1
