from collections import Counter
import sys
from pythonds import Stack

class Node:
    def __init__(self, data, frequancy):
        self.data = data
        self.frequancy = frequancy
        self.left = None
        self.right = None

class Heap( object ):
    def __init__(self,initial_size=10):
        super().__init__()
        self.cbt = [None for _ in range( initial_size )]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go
        self.codes={}

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len( self.cbt ):
            temp = self.cbt
            self.cbt = [None for _ in range( 2 * len( self.cbt ) )]

            for index in range( self.next_index ):
                self.cbt[index] = temp[index]

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = None
        self._down_heapify()

        return to_remove

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def _up_heapify(self):
        # print("inside heapify")
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_freq = self.cbt[parent_index].frequancy
            child_freq = self.cbt[child_index].frequancy

            if parent_freq > child_freq:

                self.cbt[parent_index], self.cbt[child_index] = self.cbt[child_index], self.cbt[parent_index]
                child_index = parent_index

            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            parent_freq = parent.frequancy
            left_child = None
            right_child = None
            min_element = parent_freq

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min( parent_freq, left_child.frequancy )

            # compare with right child
            if right_child is not None:
                min_element = min( right_child.frequancy, min_element )

            # check if parent is rightly placed
            if min_element == parent.frequancy:
                return

            if min_element == left_child.frequancy:
                temp = self.cbt[left_child_index]
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = temp
                parent_index = left_child_index

            elif min_element == right_child.frequancy:
                temp = self.cbt[right_child_index]
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = temp
                parent_index = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]

class Tree:
    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root

#creating heap and tree to make a tree of letters

def create_huffman_heap(data):
    heap = Heap()
    data = Counter( data )
    for elem in data:
        new_node = Node( elem, data[elem] )
        heap.insert(new_node)
    return heap

def create_huffman_tree(heap, legnth):
    x = 0
    while x < legnth:
        node1 = heap.remove()
        node2 = heap.remove()
        combine_node = Node( 0, node1.frequancy + node2.frequancy)
        combine_node.left = node1
        combine_node.right = node2
        heap.insert(combine_node)
        x = node1.frequancy + node2.frequancy
    return heap

codes = {}

def get_coded(data):
    code = ""
    for char in data:
        code += codes[char]
    return code

def huffman_encoding(data):
    if len(data) == 0 :
        print("data is empty")
        return None,None
    length_of_data = len( data ) - 1
    # create healper heap to form bianry tree
    healer_heap = create_huffman_heap( data )
    huffman = create_huffman_tree( healer_heap , length_of_data)
    huffman_tree = huffman.remove()
    huffman_tree = Tree(huffman_tree)
    make_codes_helper(huffman_tree.root,"")
    encoded = get_coded(data)

    return encoded,huffman_tree

def make_codes_helper( root, current_code):
    if(root == None):
        return
    if(root.data != 0):
        codes[root.data] = current_code
        return

    make_codes_helper(root.left, current_code + "0")
    make_codes_helper(root.right, current_code + "1")


def huffman_decoding(data, tree):
    x = 0
    root = tree.root
    decoder_stack = Stack()
    decoded_word = ""
    while x<len(data):
        if data[x]=="0":
            decoder_stack.push(root)
            root = root.left
        elif data[x]=="1":
            decoder_stack.push(root)
            root = root.right
        if root.data != 0 :
            decoded_word += root.data
            while decoder_stack.size() != 0 :
                root = decoder_stack.pop()
        x+=1
    return decoded_word

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "the bird is fly"

    print( "The size of the data is: {}\n".format( sys.getsizeof( a_great_sentence ) ) )
    print( "The content of the data is: {}\n".format( a_great_sentence ) )

    encoded_data, tree = huffman_encoding( a_great_sentence )

    print( "The size of the encoded data is: {}\n".format( sys.getsizeof( int( encoded_data, base=2 ) ) ) )
    print( "The content of the encoded data is: {}\n".format( encoded_data ) )
    try:
        decoded_data = huffman_decoding( encoded_data, tree )

        print( "The size of the decoded data is: {}\n".format( sys.getsizeof( decoded_data ) ) )
        print( "The content of the encoded data is: {}\n".format( decoded_data ) )
    except:
        pass

    a_great_sentence = "i am udacity student"

    print( "The size of the data is: {}\n".format( sys.getsizeof( a_great_sentence ) ) )
    print( "The content of the data is: {}\n".format( a_great_sentence ) )

    encoded_data, tree = huffman_encoding( a_great_sentence )

    print( "The size of the encoded data is: {}\n".format( sys.getsizeof( int( encoded_data, base=2 ) ) ) )
    print( "The content of the encoded data is: {}\n".format( encoded_data ) )
    try:
        decoded_data = huffman_decoding( encoded_data, tree )

        print( "The size of the decoded data is: {}\n".format( sys.getsizeof( decoded_data ) ) )
        print( "The content of the encoded data is: {}\n".format( decoded_data ) )
    except:
        pass

    a_great_sentence = ""
    try:
        print( "The size of the data is: {}\n".format( sys.getsizeof( a_great_sentence ) ) )
    except:
        pass
    print( "The content of the data is: {}\n".format( a_great_sentence ) )

    encoded_data, tree = huffman_encoding( a_great_sentence )
    try:
        print( "The size of the encoded data is: {}\n".format( sys.getsizeof( int( encoded_data, base=2 ) ) ) )
    except:pass
    print( "The content of the encoded data is: {}\n".format( encoded_data ) )
    try:
        decoded_data = huffman_decoding( encoded_data, tree )

        print( "The size of the decoded data is: {}\n".format( sys.getsizeof( decoded_data ) ) )
        print( "The content of the encoded data is: {}\n".format( decoded_data ) )
    except:
        pass


