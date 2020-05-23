# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.child = {}
        self.handler = None

    def insert(self,word):
        self.child[word] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self , ini):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = ini

    def insert(self,lista,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        currTrieNode = self.root
        for word in lista:
            if word not in currTrieNode.child:
                currTrieNode.insert(word)
            currTrieNode = currTrieNode.child[word]
        currTrieNode.handler =  handler

    def find(self,path ):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        pointer = self.root
        for part in path :
            if part in pointer.child:
                pointer = pointer.child[part]
            else:
                return None
        return pointer.handler


class Router:
    def __init__(self,initial):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_trie = RouteTrie(initial)


    def add_handler(self,path,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = self.split_path(path)
        self.root_trie.insert(path,handler)



    def lookup(self,path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if path == "":
            return None
        else:
            path = self.split_path(path)
            if path == []:
                return self.root_trie.root.handler
            return self.root_trie.find(path)



    def split_path(self,path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path = path.split("/")
        path = [x for x in path if x!=""]
        return path


# create the router and add a route
router = Router('root handler')  # remove the 'not found handler' if you did not implement this
router.add_handler( "/home/about", "about handler" )  # add a route

# some lookups with the expected output
print( router.lookup( "" ) )  # should print None
print( router.lookup( "/" ) )  # should print 'root handler'
print( router.lookup( "/home" ) )  # should print None
print( router.lookup( "/home/about" ) )  # should print 'about handler'
print( router.lookup( "/home/about/" ) )  # should print 'about handler'
print( router.lookup( "/home/about/me" ) )  # should print 'not found handler' or None if you did not implement one

router.add_handler( "/home/about", "new handler" )

print( router.lookup( "/home/about" ) )  # should print 'new handler'



