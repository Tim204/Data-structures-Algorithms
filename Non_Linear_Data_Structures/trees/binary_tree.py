"""
    Implementation of a Binary Tree using a Nested Node class
"""


class Tree:
    def __init__(self):
        self._root = self.Node().value

    class Node:
        def __init__(self, value=None):
            self.value = value
            self.left_child = None
            self.right_child = None

        def __str__(self):
            return f"Node = {self.value}"

        def __repr__(self):
            return self.__str__()

    def insert(self, value):
        node = self.Node(value)
        if self._root is None:
            self._root = node
            return
        current = self._root

        while True:
            if value < current.value:
                if current.left_child is None:
                    current.left_child = node
                    break
                current = current.left_child
            else:
                if current.right_child is None:
                    current.right_child = node
                    break
                current = current.right_child

    def find(self, value):
        current = self._root

        while current is not None:
            if value < current.value:
                current = current.left_child
            elif value > current.value:
                current = current.right_child
            else:
                return True
        return False

    def traverse_pre_order(self):
        """
        Similar to Method overloading in Java.
        Required to handle the private root node
        """
        self._traverse_pre_order(self._root)

    def _traverse_pre_order(self, root):
        """this method is simply implementation detail"""
        if root is None:
            return
        print(root.value)
        self._traverse_pre_order(root.left_child)
        self._traverse_pre_order(root.right_child)

    def traverse_in_order(self):
        self._traverse_in_order(self._root)

    def _traverse_in_order(self, root):
        if root is None:
            return
        self._traverse_in_order(root.left_child)
        print(root.value)
        self._traverse_in_order(root.right_child)

    def traverse_post_order(self):
        self._traverse_post_order(self._root)

    def _traverse_post_order(self, root):
        if root is None:
            return
        self._traverse_post_order(root.left_child)
        self._traverse_post_order(root.right_child)
        print(root.value)

    def height(self):
        return self._height(self._root)

    def _height(self, root):
        if root is None:
            return -1
        if self._is_leaf(root):
            return 0
        return 1 + max(self._height(root.left_child),
                       self._height(root.right_child))

    def bst_min(self):
        """For finding minimum values in Binary Search Trees"""
        if self._root is None:
            raise Exception("Tree is empty")
        current = self._root
        last = current
        while current is not None:
            last = current
            current = current.left_child
        return last.value

    def min(self):
        """Not applicable to Binary Search trees"""
        return self._min(self._root)

    def _min(self, root):
        if root is None:
            return -1
        if self._is_leaf(root):
            return root.value
        right = self._min(root.right_child)
        left = self._min(root.left_child)

        return min(min(left, right), root.value)

    def _is_leaf(self, node):
        return node.left_child is None and node.right_child is None

    def __str__(self):
        return str(self._root)


tree = Tree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)


