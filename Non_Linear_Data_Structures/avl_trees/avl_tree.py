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
        self._set_height(root)

        return self._balance(root)

    def _balance(self, root):
        if self._is_left_heavy(root):
            if self._balance_factor(root.left_child) < 0:
                root.left_child = self._rotate_left(root.left_child)  # Left rotation
            return self._rotate_right(root)
        elif self._is_right_heavy(root):
            if self._balance_factor(root.right_child) > 0:
                root.right_child = self._rotate_right(root.right_child)  # Right rotation
            return self._rotate_left(root)

        return root

    def _rotate_right(self, root):
        new_root = root.left_child
        root.left_child = new_root.right_child
        new_root.right_child = root

        self._set_height(root)
        self._set_height(new_root)  # resetting the height

        return new_root

    def _rotate_left(self, root):
        new_root = root.right_child
        root.right_child = new_root.left_child
        new_root.left_child = root

        self._set_height(root)
        self._set_height(new_root)

        return new_root

    def _set_height(self, node):
        node.height = max(self._height(node.left_child),
                          self._height(node.right_child)) + 1

    def _is_left_heavy(self, node):
        return self._balance_factor(node) > 1

    def _is_right_heavy(self, node):
        return self._balance_factor(node) < -1

    def _balance_factor(self, node):
        return 0 if node is None else \
            self._height(node.right_child) - self._height(node.right_child)

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
avl.insert(40)
