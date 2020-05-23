class TrieNode:
    def __init__(self):
        self.child ={}
        self.end_word = False

    def insert(self, char):
        self.child[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        return Trie.find(suffix)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.words = []


    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.child:
                current_node.insert(char)
            current_node = current_node.child[char]
        current_node.end_word = True

    def place_of_prefix(self,prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.child:
                return False
            curr = curr.child[char]
        return curr

    def find(self, suffix):
        if suffix == "":
            return []
        self.find_helper(suffix)
        words = self.words
        self.words = []
        return words

    def find_helper(self, prefix):

        #that get place of prefix in the trie
        placeOfPrefix = self.place_of_prefix(prefix)
        if placeOfPrefix is False:
            return

        #Base case
        if placeOfPrefix.end_word is True:
            self.words.append(prefix[1:])

        #iterate through trie to get
        for elem in placeOfPrefix.child:
            self.find_helper(prefix+elem)

        return


MyTrie = Trie()
wordList = [
     "anthology", "antagonist", "antonym","ant",
    "fun", "function", "factory",
    "trie", "trigger"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.find("fu"))
print(MyTrie.find("a"))
print(MyTrie.find(""))       #should return Empty List
print(MyTrie.find("z"))      #should return Empty list not present in trie


