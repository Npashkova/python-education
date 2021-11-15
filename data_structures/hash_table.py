"""Hash Table implementation"""
from linked_list import LinkedList


class Node:
    """Attributes: key, value, next"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Implementation of HashTable"""
    def __init__(self, size):
        self.linked_list = LinkedList()
        self.size = size

    def insert(self, new_node):
        """Add an element and key to hash table"""
        if new_node.key == self.lookup(new_node.key):
            raise KeyError("This key exists. Choose the other one.")
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.head.key = self.count_hash(new_node.key)
        else:
            last_node = self.linked_list.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
            last_node.next.key = self.count_hash(new_node.key)

    def count_hash(self, key):
        """Count hash"""
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.size

    def lookup(self, key):
        """Get value by key"""
        current = self.linked_list.head
        hash_key = self.count_hash(key)
        while current:
            if current.key == hash_key:
                return current.value
            current = current.next

    def delete(self, key):
        """Remove value by key"""
        hash_key = self.count_hash(key)
        current = self.linked_list.head
        if current.key == hash_key:
            self.linked_list.head = current.next
        else:
            while current.next:
                previous = current
                current = current.next
                if current.key == hash_key:
                    previous.next = current.next

    def show(self):
        """Show elements in hash table"""
        current = self.linked_list.head
        while current is not None:
            print(current.value, ":", current.key,  end='->')
            current = current.next


hash_table = HashTable(20)
hash_table.insert(Node('apple', 'balloon'))
hash_table.insert(Node('banana', 'sun'))
hash_table.insert(Node('tomato', 'potato'))
# hash_table.show()
# print(hash_table.lookup('tomato'))
hash_table.delete('banana')
hash_table.show()