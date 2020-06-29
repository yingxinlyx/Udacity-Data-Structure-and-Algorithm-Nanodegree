# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.isEnd = False
        self.next = {}
        self.handler = None

    def insert(self, path):
        # Insert the node as before
        if path not in self.next:
            self.next[path] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.isEnd = True
        self.root.handler = root_handler

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if paths is None or len(paths) == 0 or paths[0] != '':
            return
        node = self.root
        for i in range(1, len(paths)):
            path = paths[i]
            node.insert(path)
            node = node.next[path]
        node.isEnd = True
        node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if paths is None or len(paths) == 0 or paths[0] != '':
            return None
        node = self.root
        for i in range(1, len(paths)):
            path = paths[i]
            if path not in node.next:
                return None
            node = node.next[path]

        if node.isEnd:
            return node
        return None


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        paths = self.split_path(path)
        self.routeTrie.insert(paths, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        paths = self.split_path(path)
        node = self.routeTrie.find(paths)
        if node is None:
            return self.not_found_handler
        return node.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path is None:
            return []
        paths = path.split('/')
        if len(paths) > 1 and paths[-1] == '':
            paths.pop()
        return paths


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup(""))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler'
print(router.lookup("/home/about/me"))  # should print 'not found handler'
print(router.lookup("abc"))  # should print 'not found handler'
