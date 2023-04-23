
class Array:
    def __init__(self, length):
        self._size = length
        self.array = []
        self._indexes = []

    def insert(self, item):
        if len(self.array) != self._size:
            self.array.append(item)
        else:
            self._size += 1
            self.array.append(item)

    def _index_list(self):
        if len(self.array) != 0:
            for index in self.array:
                self._indexes.append(self.array.index(index))

    def indexOf(self, number):
        if number in self.array:
            return self.array.index(number)
        return -1

    def remove_at(self, index):
        if len(self.array) != 0:
            if index in self._indexes:
                self.array.remove(self.array[index])
            else:
                print(-1)
        else:
            return -1

#
ar = Array(3)
ar.insert(15)
ar.insert(20)
ar.insert(50)
ar.insert(155)
ar.insert(160)
print(ar.indexOf(160))


print(ar.array)







