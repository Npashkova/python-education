"""Queue implementation"""


class Node:
    """Store value and a link to the next"""
    def __init__(self, element=None, next_el=None):
        self.element = element
        self.next = next_el


class Queue:
    """Implementation of queue """
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, new_node):
        """Insert element to the end of queue"""
        if self.first is None:
            self.first = Node(new_node)
            self.last = self.first
        else:
            self.last.next = Node(new_node)
            self.last = self.last.next

    def dequeue(self):
        """Remove element from the head of queue"""
        if self.first is None:
            return None
        del_node = self.first
        self.first = self.first.next
        return del_node

    def show(self):
        """Shows queue"""
        node = self.first
        while node is not None:
            print(node.element, end='->')
            node = node.next

    def peek(self):
        """Get element from the head"""
        if self.first is None:
            return None
        return self.first.element


queue = Queue()
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(8)
# queue.show()
queue.dequeue()
# queue.show()
print(queue.peek())

