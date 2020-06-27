I'm not quite sure about this question. The explanation use set while the test case has duplicates in a list.
So I treat it as multiset. Union and intersection are based on the corresponding definition of multiset https://en.wikipedia.org/wiki/Multiset#Basic_properties_and_operations.

For intersection, I use a hash map to count the frequency of each element of list1. For elements in list2, only those also in the hash map is added to result. And also when add an element, decrement the frequency of this element in the hash map so I won't add too many.

For union, I add all elements in list1 to result and also use a hash map to count the frequency of each element. For each element in list2, if it's not in the hash map, it should be added to result, otherwise just decrement the frequency of this element in the hash map until the frequency is zero, when I remove the element from the hash map.

Assume length of list1 is m and length of list 2 is n.
Time complexity of union and intersection are both O(m+n), since every element in list1 and list2 is iterated.
Space complexity of union and intersection are also O(m+n), it's just the space the hash map uses.