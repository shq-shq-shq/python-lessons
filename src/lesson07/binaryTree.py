import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def searchRecursive(self, value):
        if self.value == value:
            print("    NODE: !%s!" % self.value)
            return (True, self)
        elif value < self.value:
            if self.left is None:
                print("    NODE: None<-%s" % self.value)
                return (False, self)
            else:
                print("    NODE: <-%s" % self.value)
                return self.left.searchRecursive(value)
        else:
            if self.right is None:
                print("    NODE: %s->None" % self.value)
                return (False, self)
            else:
                print("    NODE: %s->" % self.value)
                return self.right.searchRecursive(value)

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
        print("tree: add %s" % value)
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def addAll(self, values):
        for v in values:
            self.add(v)

    def contains(self, value):
        print("tree: search %s" % value)
        if self.root is None:
            return False
        else:
            return self.root.contains(value)


tree = BinaryTree()

numbers = list(range(55)) + list(range(56, 101, 2))
random.shuffle(numbers)
tree.addAll(numbers)

print(tree.contains(10))
print(tree.contains(55))
print(tree.contains(1000))
