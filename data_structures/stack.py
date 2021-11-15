"""Stack implementation"""


class Node:
    """Store value and a link to the next"""
    def __init__(self, element=None, next_el=None):
        self.element = element
        self.next = next_el


class Stack:
    """Creating stack with classical methods"""
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, element):
        """Add value to the end of stack"""
        if self.first is None:
            self.first = Node(element)
            self.last = self.first
        else:
            self.last.next = Node(element)
            self.last = self.last.next

    def pop(self):
        """Remove and show last element"""
        element = self.first
        self.first = self.first.next
        return element.element

    def peek(self):
        """Show last stack element"""
        return self.last.element

    def show(self):
        """Shows stack"""
        node = self.first
        while node is not None:
            print(node.element, end='->')
            node = node.next


stack = Stack()
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
# stack.show()
print(stack.pop())
print(stack.pop())
# print(stack.pop())
# print(stack.peek())



