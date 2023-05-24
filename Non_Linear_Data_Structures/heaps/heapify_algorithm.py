"""
    Transforming an Array into a heap in place
"""

class MaxHeap:
    @classmethod
    def heapify(cls, array):
        i = 0
        while i < len(array):
            cls._heapify(array, i)
            pass

    @classmethod
    def _heapify(cls, array, index):
        largest_index = index
        left_index = index * 2 + 1
        right_index = index * 2 + 2

        if left_index < len(array) and \
                array[left_index] > array[largest_index]:
            largest_index = left_index

        if right_index < len(array) and array[right_index] > array[largest_index]:
            largest_index = right_index

        if index == largest_index:
            return

