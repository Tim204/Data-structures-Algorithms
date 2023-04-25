

class ListQueue:
    """Implementing Queues using a python list"""
    def __init__(self):
        self._list = []
        self._item_count = 0

    def enqueue(self, item):
        self._list.append(item)
        self._item_count += 1

    def dequeue(self):
        if self._item_count != 0:
            self._item_count -= 1
            return self._list.pop(0)
        return None

    def peek(self):
        if self._item_count != 0:
            return self._list[0]
        return None

    def size(self):
        return self._item_count


queue = ListQueue()
queue.enqueue(10)
queue.enqueue(12)
queue.enqueue(100)

print(queue.dequeue())
print(queue.size())





