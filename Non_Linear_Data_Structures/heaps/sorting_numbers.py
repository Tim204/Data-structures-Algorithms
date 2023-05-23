from heaps import Heap

"""
    Sorting numbers using heaps
"""


class Sort:
    def __init__(self, array):
        self._array = array

    def _populated_heap(self):
        heap = Heap()
        for number in self._array:
            heap.insert(number)
        return heap

    def descending_order(self):
        heap = self._populated_heap()
        descending = []
        while not heap.is_empty():
            descending.append(heap.remove())
        return descending

    def ascending_order(self):
        heap = self._populated_heap()
        temp = []
        while not heap.is_empty():
            temp.append(heap.remove())
        return [a for a in temp[::-1]]


sort = Sort([5, 3, 10, 1, 4, 2])
print(sort.descending_order())
print(sort.ascending_order())

