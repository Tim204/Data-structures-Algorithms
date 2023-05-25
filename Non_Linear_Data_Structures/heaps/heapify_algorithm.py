"""
    Transforming an Array into a heap in place
"""
from Non_Linear_Data_Structures.heaps.heaps import Heap


class MaxHeap:
    @classmethod
    def heapify(cls, array):
        last_parent_index = int((len(array) / 2) - 1)
        i = last_parent_index
        while i >= 0:
            cls._heapify(array, i)
            i -= 1

    @classmethod
    def _heapify(cls, array, index):
        largest_index = index
        left_index = index * 2 + 1
        right_index = index * 2 + 2

        if left_index < len(array) and \
                array[left_index] > array[largest_index]:
            largest_index = left_index

        if right_index < len(array) and \
                array[right_index] > array[largest_index]:
            largest_index = right_index

        if index == largest_index:
            return
        cls._swap(array, index, largest_index)
        # Recursively repeating this step while going down the subtrees
        # until the largest item is in the right position
        cls._heapify(array, largest_index)

    @classmethod
    def _swap(cls, array, first_index, second_index):
        temp = array[first_index]
        array[first_index] = array[second_index]
        array[second_index] = temp

    @classmethod
    def get_kth_largest(cls, array, k):
        """
            Finds The kth largest number on an array using a heap
        """
        if k < 1 or k > len(array):
            raise IndexError(f"{k} is out of range")
        heap = Heap()
        i = 0
        for item in array:
            heap.insert(item)
        while i < k - 1:
            heap.remove()
            i += 1
        return heap.max()


numbers = [5, 3, 8, 4, 1, 2]

# MaxHeap.heapify(numbers)
print(MaxHeap.get_kth_largest(numbers, 1))

print(numbers)


