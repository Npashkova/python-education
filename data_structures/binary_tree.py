"""Binary tree implementation"""


class Node:
    """Store links and values"""
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """Attributes: root
    Methods: insert lookup delete
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Add value to root"""
        if self.root is None:
            self.root = Node(value)
        else:
            self.__add(value, self.root)

    def __add(self, value, node):
        """Append value recursively"""
        if value < node.value:
            if node.left is not None:
                self.__add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self.__add(value, node.right)
            else:
                node.right = Node(value)

    def lookup(self, value):
        """Find and return value"""
        if self.root is not None:
            return self.__search(value, self.root)
        return None

    def __search(self, value, node):
        """Search for value recursively"""
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self.__search(value, node.left)
        elif value > node.value and node.right is not None:
            return self.__search(value, node.right)

    def delete(self, value):
        """Delete value"""
        if self.root is None:
            return
        if self.root is not None:
            node = self.root
            self.__del(value, node)

    def __del(self, value, node):
        """Delete value recursively"""
        if value < node.value:
            node.left = self.__del(value, node.left)
        elif value > node.value:
            node.right = self.__del(value, node.right)
        else:
            if node.left is None and node.right is None:
                if self.root == node:
                    self.root = None
                    return self.root
                node = None
                return node
            if node.left is None:
                if self.root == node:
                    self.root = node.right
                    return self.root
                node = node.right
                return node
            if node.right is None:
                if self.root == node:
                    self.root = node.left
                    return self.root
                node = node.left
                return node

            point = node.right
            while point.left is not None:
                point = point.left
            new_node = point
            node.value = new_node.value
            node.right = self.__del(new_node.value, node.right)
        return node


tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
print(tree.lookup(2))
tree.delete(2)
print(tree.lookup(2))
