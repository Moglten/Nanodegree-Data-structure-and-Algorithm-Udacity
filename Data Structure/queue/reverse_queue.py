def reverse_queue(queue):
    """
    Given a Queue to reverse its elements

    Args:
       queue : queue gonna reversed
    Returns:
      queue : Reversed Queue
    """
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())
