# Solution
def skip_i_delete_j(head, i, j):
    """
    Given a head of LinkedList, delete from that linkedList index j and skip index i iterative

    Args:
       head : head of LinkedList
       i : index will be skipped
       j : index will be deleted
    Returns:
      head : Return the head of new LinkedList
    """
    if i == 0:
        return None
    
    if head is None or j < 0 or i < 0:
        return head
    
    current = head
    previous = None
    while current:
        # skip (i - 1) nodes
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next
        
        # delete next j nodes
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        previous.next = current
    return head