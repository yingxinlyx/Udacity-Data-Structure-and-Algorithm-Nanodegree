For intersection, I put all elements of list1 in a set. For elements in list2, only those also in the set is added to result. And also when add an element, remove it from the set to avoid duplicates.

For union, I use a set to avoid duplicates. For each element in list1 or list2, it is added to result only if it's not already in the set, and add it to the set to keep track of unique elements.

Assume length of list1 is m and length of list 2 is n.
Time complexity of union and intersection are both O(m+n), since every element in list1 and list2 is iterated.
Space complexity of union and intersection are also O(m+n), it's just the space the hash map uses.