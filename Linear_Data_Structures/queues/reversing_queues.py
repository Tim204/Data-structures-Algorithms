from queue import Queue
from Linear_Data_Structures.stacks.stacks import Stack


class QReverser:
    """Reverting a queue using Stacks"""
    def __init__(self, queue):
        self._queue = queue

    def reverse(self):
        stack = Stack()
        while not self._queue.empty():
            stack.push(self._queue.get())
        while not stack.is_empty():
            self._queue.__setitem__(stack.pop())
        return self._queue.queue


queue = Queue()
queue.put(10)
queue.put(20)
queue.put(30)

queue_reverser = QReverser(queue)
print(f"Original queue: {queue.queue}\n")
print(f"Reversed queue: {queue_reverser.reverse()}")

