
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def searchRecursive(self, value):
        if self.value == value:
            return (True, self)
        elif value < self.value:
            if self.left is None:
                return (False, self)
            else:
                return self.left.search(value)
        else:
            if self.right is None:
                return (False, self)
            else:
                return self.right.search(value)

    def contains(self, value):
        found, node = self.searchRecursive(value)
        return found

    def add(self, value):
        found, node = self.searchRecursive(value)

        if found:
            return False
        else:
            if value < node.value:
                node.left = Node(value)
            else:
                node.right = Node(value)

            return True

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def contains(self, value):
        if self.root is None:
            return False
        else:
            return self.root.contains(value)