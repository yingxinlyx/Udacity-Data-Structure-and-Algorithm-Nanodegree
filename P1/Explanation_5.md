I implement it as a linked list where the data of the list node is a block object. And I add block to the head of the list since it should point to the previous block.

To add a block to the block chain, the time complexit is O(1), since it's the same as add a node to the head of linked list. And space complexity is also O(1) since it just creates a new list node.