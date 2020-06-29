# %%
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.isEnd = False
        self.next = {}

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.next:
            self.next[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        res = []
        if self.isEnd and len(suffix) != 0:
            res.append(suffix)
        for ch in self.next:
            res.extend(self.next[ch].suffixes(suffix + ch))
        return res


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        node = self.root
        for ch in word:
            node.insert(ch)
            node = node.next[ch]
        node.isEnd = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        node = self.root
        for ch in prefix:
            if ch not in node.next:
                return None
            node = node.next[ch]
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# %%
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')
