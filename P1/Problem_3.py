import sys
from queue import PriorityQueue


class TreeNode:
    def __init__(self, char):
        self.value = char
        self.left = None
        self.right = None


def build_tree(d):
    if len(d) == 0:
        return None
    pq = PriorityQueue()
    for ch in d.keys():
        pq.put((d[ch], ch, TreeNode(ch)))

    if pq.qsize() == 1:
        freq, ch, node = pq.get()
        root = TreeNode(freq)
        root.left = node
        return root

    while pq.qsize() > 1:
        a = pq.get()
        b = pq.get()
        value = a[2].value + b[2].value
        node = TreeNode(value)
        node.left = a[2]
        node.right = b[2]
        pq.put((a[0]+b[0], value, node))

    return pq.get()[2]


def traverse(root, d):

    def dfs(node, encode, d):
        if node is None:
            return
        if node.left is None and node.right is None:
            d[node.value] = encode
            return

        dfs(node.left, encode+"0", d)
        dfs(node.right, encode+"1", d)

    dfs(root, "", d)


def huffman_encoding(data):
    freq = {}
    for ch in data:
        freq[ch] = freq.get(ch, 0) + 1

    root = build_tree(freq)

    encode = {}
    traverse(root, encode)

    code = ""
    for ch in data:
        code += encode[ch]

    return code, root


def huffman_decoding(data, tree):
    if len(data) == 0:
        return ""

    node = tree
    decode = ""
    i = 0
    data += "#"
    while i < len(data):
        if node.left is None and node.right is None:
            decode += node.value
            node = tree
            continue
        if data[i] == "0":
            node = node.left
        else:
            node = node.right
        i += 1

    return decode


if __name__ == "__main__":
    # test case 1
    test1 = "The bird is the word"
    print("The content of the data is: {}\n".format(test1))

    encoded_data, tree = huffman_encoding(test1)
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The content of the decoded data is: {}\n".format(decoded_data))

    # test case 2
    test2 = "xxxxx"
    print("The content of the data is: {}\n".format(test2))

    encoded_data, tree = huffman_encoding(test2)
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The content of the decoded data is: {}\n".format(decoded_data))

    # test case 3
    test3 = "aabbccdd"
    print("The content of the data is: {}\n".format(test3))

    encoded_data, tree = huffman_encoding(test3)
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The content of the decoded data is: {}\n".format(decoded_data))
