# %%
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    s = set()
    llist = LinkedList()
    node = llist_1.head
    while node:
        if node.value not in s:
            llist.append(node.value)
        s.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value not in s:
            llist.append(node.value)
        s.add(node.value)
        node = node.next

    return llist


def intersection(llist_1, llist_2):
    llist = LinkedList()
    s1 = set()
    s2 = set()
    node = llist_1.head
    while node:
        s1.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        s2.add(node.value)
        node = node.next

    for i in s2:
        if i in s1:
            llist.append(i)

    return llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
