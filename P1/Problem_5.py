import hashlib
import time


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        str = self.timestamp + self.data + self.previous_hash
        hash_str = str.encode('utf-8')
        sha = hashlib.sha256()
        sha.update(hash_str)
        return sha.hexdigest()


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class BlockChain:
    def __init__(self):
        self.head = None

    def add(self, data):
        previous_hash = ""
        if self.head is not None:
            previous_hash = self.head.data.hash

        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        node = ListNode(Block(timestamp, data, previous_hash))
        node.next = self.head
        self.head = node

        return self


# test case 1
s1 = "first data"
s2 = "second data"
s3 = "third data"

blockChain = BlockChain()
blockChain.add(s1).add(s2).add(s3)

node = blockChain.head
while node:
    print(node.data.data)
    print(node.data.hash)
    print(node.data.previous_hash)
    node = node.next
# any node's previous hash should be the hash of next node

# test case 2
s1 = "aaa"
s2 = "aaa"
s3 = "aaa"

blockChain = BlockChain()
blockChain.add(s1).add(s2).add(s3)

node = blockChain.head
while node:
    print(node.data.data)
    print(node.data.hash)
    print(node.data.previous_hash)
    node = node.next
# even though the data is the same, hash should be different

# test case 3
blockChain = BlockChain()

node = blockChain.head
while node:
    print(node.data.data)
    print(node.data.hash)
    print(node.data.previous_hash)
    node = node.next
# no output
