Both add_handler and lookup function need to do split_path first. When I get the splited list, it is easy to insert to trie or find in trie. Just treat one element in the list as a charactor in a string as problem 5.

For time and space complexity, both functions depend on split_path which takes O(n) time and also O(n) space, where n is the length of the path. add_handler then insert path to the trie, which takes O(n) time and also O(n) space. So the overall time complexity of add_handler is O(n) and space complexity is O(n). lookup function then find in the trie, which take O(n) time and O(1) space. So the overall time complexity of lookup is O(n) and space complexity is O(n).