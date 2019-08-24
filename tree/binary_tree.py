class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left is not None:
            for node in self.left:
                yield node

        yield self.value

        if self.right is not None:
            for node in self.right:
                yield node

    def repr(self):
        return f'Node {self.value}, {self.left}, {self.right}'


class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        self.root = BinarySearchTree.__insert(self.root, value)

    def __insert(root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = BinarySearchTree.__insert(root.left, value)
        else:
            root.right = BinarySearchTree.__insert(root.right, value)

        return root

    def __iter__(self):
        if self.root is not None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return f'BinarySearchTree {repr(self.root)}'


def main():
    list_input = input("Enter list of numbers: ")
    list_number = list_input.split()
    tree = BinarySearchTree()

    for element in list_number:
        tree.insert(float(element))

    for node in tree:
        print(node)


if __name__ == "__main__":
    main()
