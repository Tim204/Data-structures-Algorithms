
class PriorityQueue:
    """Priority queue implementation using a list"""
    def __init__(self):
        self._queue = []
        self.size = 0
        self._length = len(self._queue[::-1])

    def enqueue(self, item):
        if self.is_empty():
            self._queue.append(item)
        for i in range(self._length - 1):
            if self._queue[i] > item:
                self._queue[i::-1 + 1] = self._queue[i]
            else:
                break

    def is_empty(self):
        return self.size == 0

    def get_queue(self):
        return self._queue


pq = PriorityQueue()
pq.enqueue(12)
pq.enqueue(11)
pq.enqueue(13)

print(pq.get_queue())

num = [1, 2, 3]
print(len(num))