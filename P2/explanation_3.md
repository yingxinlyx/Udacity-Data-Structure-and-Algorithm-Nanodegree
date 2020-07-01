To form one biggest number, it's always optimal to put the largest digit as first digit, put the second largest digit as the second digit, and so on. So I first sort the digits in descending order. Because the number of digits in the two numbers cannot differ by more than one, so I distribute digits evenly. Since the sum should be maximum, I put largest digit to number 1 and second largest digit to number 2 and so on.

The sorting algorithm is a typical merge sort.

Time complexity and space complexity are both O(nlogn) where n is the length of the input array, since merge sort is used.