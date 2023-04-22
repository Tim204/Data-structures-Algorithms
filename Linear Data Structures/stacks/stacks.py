class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """Implementation of Stacks using a Linked list"""
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, data):
        node = Node(data)
        if self._head is None:
            self._head = node
        else:
            node.next = self._head
            self._head = node
        self._size += 1

    def pop(self):
        if self._head is None:
            raise Exception("No items in the stack")
        removed_value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return removed_value

    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self._head.value

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def print_stack(self):
        first_node = self._head
        while first_node:
            print(first_node.value)
            first_node = first_node.next





