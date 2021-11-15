"""Linked list implementation"""


class Node:
    """Store value and a link to the next"""
    def __init__(self, element=None, next_el=None):
        self.element = element
        self.next = next_el


class LinkedList:
    """Realise logic of linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def show(self):
        """Show linked list"""
        cur_element = self.head
        while cur_element is not None:
            print(cur_element.element, end='->')
            cur_element = cur_element.next

    def prepend(self, new_node):
        """Add an element to the beginning"""
        if self.head is None:
            self.head = Node(new_node)
            self.tail = self.head
        else:
            self.head = Node(new_node, self.head)

    def append(self, new_node):
        """Add an element to the end"""
        if self.head is None:
            self.head = Node(new_node)
            self.tail = self.head
        else:
            self.tail.next = Node(new_node)
            self.tail = self.tail.next

    def lookup(self, element):
        """Returns index of the first found element"""
        last_node = self.head
        index = 0
        while last_node is not None:
            if last_node.element == element:
                return index
            index += 1
            last_node = last_node.next
        return f"'{element}' not found"

    def insert(self, index, element):
        """Insert element to the specified index"""
        if self.head is None:
            self.tail = self.head = Node(element)
            return
        if index == 0:
            self.head = Node(element, self.head)
            return
        cur_element = self.head
        count = 0
        while cur_element is not None:
            count += 1
            if count == index:
                cur_element.next = Node(element, cur_element.next)
                if cur_element.next.next is None:
                    self.tail = cur_element.next
                break
            cur_element = cur_element.next

    def delete(self, index):
        """Delete element by index"""
        count = 0
        start_node = self.head
        pre_node = None
        if index == 0:
            self.head = start_node.next
            return
        while count < index and start_node is not None:
            pre_node = start_node
            start_node = start_node.next
            count += 1
        pre_node.next = start_node.next
        del start_node


# linked_list = LinkedList()
# linked_list.append(3)
# linked_list.append(2)
# linked_list.append(4)
# linked_list.append(8)
# linked_list.append(12)
# linked_list.append(7)
# linked_list.prepend(0)
# print(linked_list.show())
# linked_list.prepend(6)
# linked_list.delete(4)
# linked_list.insert(3, 8)
# print(linked_list.show())
# print(linked_list.lookup(6))
