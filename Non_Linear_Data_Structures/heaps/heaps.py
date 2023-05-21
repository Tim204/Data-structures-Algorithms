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

    def remove(self):
        if self.is_empty():
            raise Exception("Can't remove items from an empty heap")

        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        index = 0

        while index <= self.size and not self._parent_is_valid(index):
            higher_child_index = self._higher_child_index(index)
            self._swap(index, higher_child_index)
            index = higher_child_index

    def _higher_child_index(self, index):
        if not self._has_left_child(index):
            return index

        if not self._has_right_child(index):
            return self._left_child_index(index)

        return self._left_child(index) \
            if self._left_child_index(index) > self._right_child_index(index) \
            else self._right_child_index(index)

    def _has_left_child(self, index):
        return self._left_child_index(index) <= self.size

    def _has_right_child(self, index):
        return self._right_child_index(index)

    def _parent_is_valid(self, index):
        if not self._has_left_child(index):
            return True
        if not self._has_right_child(index):
            return self.items[index] >= self._left_child(index)

        return self.items[index] >= self._left_child(index) \
            and self.items[index] >= self._right_child(index)

    def _left_child(self, index):
        return self.items[self._left_child_index(index)]

    def _right_child(self, index):
        return self.items[self._right_child_index(index)]

    def _left_child_index(self, index):
        return index * 2 + 1

    def _right_child_index(self, index):
        return index * 2 + 2

    def is_full(self):
        return self.size == self._limit

    def is_empty(self):
        return self.size == 0

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
heap.remove()


print(heap.items)
