from Linear_Data_Structures.stacks.stacks import Stack


class QueueStack:
    """Implementing a queue using two stacks"""
    def __init__(self):
        self._first_stack = Stack()
        self._second_stack = Stack()

    def enqueue(self, data):
        self._first_stack.push(data)

    def dequeue(self):
        if self._second_stack.is_empty():
            while not self._first_stack.is_empty():
                self._second_stack.push(self._first_stack.pop())
        return self._second_stack.pop()

    def peek(self):
        return self._second_stack.peek()

    def is_empty(self):
        return self._first_stack.is_empty()

    def is_full(self):
        return not self._first_stack.is_empty()

