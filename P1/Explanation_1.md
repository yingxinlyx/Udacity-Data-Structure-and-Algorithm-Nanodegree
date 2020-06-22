For this problem, I used 2 data structures: hashmap and doubly-linked list. 

The key of hashpmap stored the cache index (key), the value of hashmap stored a doubly-linked list node, in which I was able to keep track the most recently used item as well as head and tail manipulation. 

In my program, head is the most recently used item and tail is the least recently used one. For a head node, its prev will always be None, whereas for a tail node, its next will always be None. 

Except `set()` and `get()` functions, I also defined `_set_head()`, `_remove_node()` and `_remove_LRU()` functions to make the program more readable. 


Time complexity of `set()`: add an item in a hashmap, O(1)

Space complexity of `set()`: capacity of the hashmap, O(n)

Time complexity of `get()`: retrieve an item from a hashmap, O(1)

Space complexity of `get()`: allocate one item, O(1)
