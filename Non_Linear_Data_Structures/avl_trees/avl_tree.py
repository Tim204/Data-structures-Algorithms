class AVLNode:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0

    def __str__(self):
        return f"Node = {self.value}"

    def __repr__(self):
        return self.__str__()


class AVLTree:
    def __init__(self):
        self._root = AVLNode().value

    def insert(self, value):
        self._root = self._insert(self._root, value)

    def _insert(self, root, value):
        """Implementing the insert method recursively"""
        if root is None:
            return AVLNode(value)
        if value < root.value:
            root.left_child = self._insert(root.left_child, value)
        else:
            root.right_child = self._insert(root.right_child, value)
        root.height = max(self._height(root.left_child),
                          self._height(root.right_child)) + 1
        return root

    def _height(self, node):
        return -1 if node is None else node.height

    def __str__(self):
        return str(self._root)

    def __repr__(self):
        return self.__str__()


avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(30)






