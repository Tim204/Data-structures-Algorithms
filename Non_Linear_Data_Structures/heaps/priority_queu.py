from heaps import Heap


class PriorityQueue:
    """Implementing priority queues using heaps"""
    def __init__(self):
        self._heap = Heap()

    def enqueue(self, item):
        self._heap.insert(item)

    def dequeue(self):
        return self._heap.remove()

    def is_empty(self):
        return self._heap.is_empty()


