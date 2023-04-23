from queue import Queue


class QReverser:
    def __init__(self, queue):
        self._queue = queue

    def reverse(self):
        q = []
        for i in self._queue.queue:
            q.append(i)
        return q


queu = Queue()
queu.put(10)
queu.put(20)
queu.put(30)
queu.get()

rev = QReverser(queu)
print(rev.reverse())


