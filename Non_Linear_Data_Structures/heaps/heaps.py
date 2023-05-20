"""
    Implementing a Heap using a list
"""


class Heap:
    def __init__(self, heap_limit=10):
        self.items = []
        self.size = 0
        self._limit = heap_limit

    def insert(self, value):
        if self.is_full():
            raise Exception("The limit has been reached")

        self.items.append(value)
        self.size += 1
        self._bubble_up()

    def is_full(self):
        return self.size == self._limit

    def _bubble_up(self):
        """Moving up the big values to satisfy the heap property"""
        index = self.size - 1
        while index > 0 and self.items[index] > self.items[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _parent(self, index):
        return int((index - 1) / 2)

    def _swap(self, first_index, second_index):
        temporary = self.items[first_index]
        self.items[first_index] = self.items[second_index]
        self.items[second_index] = temporary


heap = Heap()
heap.insert(10)
heap.insert(5)
heap.insert(17)
heap.insert(4)
heap.insert(22)

print(heap.items)
