steps of encoding:
1. count the frequency of each charactor
2. build a encode tree using heap
3. traverse the encode tree to get the code of each charactor
4. form an encoded string

time complexity and space complexity analysis of huffman_encoding:
assume n = length of input data
step 1 takes O(n) time and O(n) space
for step 2, if number of distinct charactor is x, while loop will execute x-1 times, so time complexity is O(x+x-1) = O(x), since x = O(n),
time comlexity is O(n). step 2 creates totally 2x-1 nodes, so space complexity is O(n)
for step 3, visit each node only once, so time complexity is O(n). extra space is the hash map, so space complexity is O(n)
step 4 takes O(n) time and no extra space
overall, time complexity is O(n), space complexity is O(n)

step of decoding:
traverse the encode tree according to each bit of input data. when a leaf node is reached, put the charactor to output and go from root again.

for huffman_decoding, time complexity is O(n) where n is the length of input data, space complexity is O(1)