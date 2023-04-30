
"""
    Implementation of a Hash Table(Dictionary) from scratch, using Python.

    The process Requires 3 things to successfully solve the problem:
        1- A hash function that will take a key as input and output an index.
        2- A storage which will be used to hold the key-value pairs
        3- How to deal with hash collisions
"""


class HashTable:

    def __init__(self, size=1000):
        """
            using python list as storage, each list element is also a list,
            which helps in solving hash collisions
        """
        self._storage = [[] for _ in range(size)]
        self._size = size
        self._length = 0

    def put(self, key, value):
        self.__setitem__(key, value)

    def get(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            return None

    def remove(self, key):
        self.__delitem__(key)

    def keys(self):
        return self.__iter__()

    def values(self):
        for key_var in self._key_val_iterator():
            yield key_var[1]

    def items(self):
        return self._key_val_iterator()

    def __setitem__(self, key, value):
        for list_element in self._storage[self._compute_index(key)]:
            if key == list_element[0]:  # already exist, update its value
                list_element[1] = value
                break
        else:
            self._storage[self._compute_index(key)].append([key, value])
            self._length += 1

    def __getitem__(self, key):
        for list_element in self._storage[self._compute_index(key)]:
            if list_element[0] == key:
                return list_element[1]

        raise KeyError(f'Key {key} does not exist')

    def __delitem__(self, key):
        for sub_lst in self._storage[self._compute_index(key)]:
            if key == sub_lst[0]:
                self._storage[self._compute_index(key)].remove(sub_lst)
                self._length -= 1
                return

        raise KeyError(f'Key "{key}" does not exist')

    def __contains__(self, key):
        for item in self._storage[self._compute_index(key)]:
            if item[0] == key:
                return True
        return False

    def __len__(self):
        return self._length

    def __iter__(self):
        for key_var in self._key_val_iterator():
            yield key_var[0]

    def _key_val_iterator(self):
        for sub_lst in self._storage:
            if not sub_lst:
                continue
            for item in sub_lst:
                yield item

    def _compute_index(self, key):
        return hash(key) % self._size

    def __str__(self):
        res = []
        for ele in self._storage:
            for key_value in ele:
                if isinstance(key_value[0], str):
                    key_str = f'\'{key_value[0]}\''
                else:
                    key_str = f'{key_value[0]}'
                if isinstance(key_value[1], str):
                    value_str = f'\'{key_value[1]}\''
                else:
                    value_str = f'{key_value[1]}'

                res.append(f'{key_str}: {value_str}')
        key_value_pairs_str = '{}'.format(', '.join(res))
        return '{' + key_value_pairs_str + '}'

    def __repr__(self):
        return self.__str__()


dic = HashTable()
dic["name"] = "John"
dic.put("age", 20)
dic.remove("age")

print(dic)





