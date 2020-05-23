class GraphNode( object ):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append( new_node )

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove( del_node )


class Graph( object ):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child( node2 )
            node2.add_child( node1 )

    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child( node2 )
            node2.remove_child( node1 )

#-----------------------------------------------------------

#bfs iteration

def bfs_search(root_node, search_value):
    visited_set = {root_node}
    organizer_queue = []

    if root_node.value == search_value:
        return root_node.value

    curr_node = root_node
    try:

        while len(organizer_queue) >= 0 :
            for node in curr_node.children:
                if node.value == search_value:
                    return node.value
                if node not in visited_set:
                    visited_set.add(node)
                    organizer_queue.insert( 0, node )

            curr_node = organizer_queue.pop()

    except :
        return "not exist"

#-----------------------------------------------------------


#-----------------------------------------------------------

#dfs RECURSIONALY

def dfs_recursion_start(start_node):
    visited = {start_node}
    dfs_recursion(start_node,visited)

def dfs_recursion(node,visited):

    for subnode in node.children :
        if subnode not in visited:
            visited.add(subnode)
            dfs_recursion(subnode, visited )
    print( node.value )

#-----------------------------------------------------------

#-----------------------------------------------------------

#dfs interation

def dfs_search(root_node, search_value):
    seen_node = {root_node}
    reversing_stack = []
    reversing_stack.append(root_node)
    curr_node = root_node

    while len(reversing_stack) >= 1 :
        if curr_node.value == search_value:
            return curr_node.value

        for node in curr_node.children:
            if node not in seen_node:
                seen_node.add(node)
                reversing_stack.append( node )
        curr_node = reversing_stack.pop()

    return False

#-----------------------------------------------------------


