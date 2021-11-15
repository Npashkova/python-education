"""Graph implementation"""


class Node:
    """Store links and values"""
    def __init__(self, vertex):
        self.vertex = vertex
        self.store = None
        self.next = None


class LinkedList:
    """Realise logic of linked list"""
    def __init__(self):
        self.head = None

    def append(self, new_node):
        """Add an element to the end"""
        if self.head:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
        else:
            self.head = new_node


class Graph:
    """Implement Undirected Graph"""
    def __init__(self, verticals):
        self.verticals = verticals
        self.graph = None

    def insert(self, source, destination):
        """Add a node and links to other nodes"""
        node = Node(destination)
        node.next = self.__lookup(source)
        self.__insert(node, source)
        node = Node(source)
        node.next = self.__lookup(destination)
        self.__insert(node, destination)

    def __lookup(self, index):
        """Find the index of an element"""
        index_counter = 0
        last_node = self.graph.head
        while last_node and index_counter != index:
            last_node = last_node.next
            index_counter += 1
        return last_node.store

    def __insert(self, data, index):
        """Insert an element at place you need"""
        count = 0
        start_node = self.graph.head
        while count < index:
            start_node = start_node.next
            count += 1
        start_node.store = data

    def show(self):
        """Show graph elements"""
        current = self.graph.head
        for i in range(self.verticals):
            print(f'Vertex {i}')
            while current.store:
                print(' -> {}'.format(current.store.vertex), end="")
                current.store = current.store.next
            if current.next:
                current = current.next
            print('\n')

    def lookup(self, value):
        """find a node by value and return its link"""
        counter = 0
        last_node = self.graph.head
        while last_node and counter != value:
            last_node = last_node.next
            counter += 1
        return last_node


linked_list = LinkedList()
linked_list.append(Node(2))
linked_list.append(Node(3))
linked_list.append(Node(4))
linked_list.append(Node(7))
linked_list.append(Node(8))
linked_list.append(Node(9))

graph = Graph(5)
graph.graph = linked_list
graph.insert(0, 1)
graph.insert(0, 4)
graph.insert(1, 2)
graph.insert(1, 3)
graph.insert(1, 4)
graph.insert(2, 3)
graph.insert(3, 4)
graph.show()
print(graph.lookup(2))
