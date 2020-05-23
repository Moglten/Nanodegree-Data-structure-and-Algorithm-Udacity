
def create_linked_list_better(input_list):
    '''
    :param input_list: list of element wanna convert it to Linkedlist
    :return: the head of created linkedList
    here New Feature of tail to detect obviously the tail
    '''
    head = None
    tail = None
    
    for value in input_list:
        
        if head is None:
            head = Node(value)
            tail = head # when we only have 1 node, head and tail refer to the same node
        else:
            tail.next = Node(value) # attach the new node to the `next` of tail
            tail = tail.next # update the tail
            
    return head