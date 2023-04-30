
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
            which helps in solving hash conflict
        """
        self._storage = [[] for _ in range(size)]
        self._size = size
        self._length = 0

    def __setitem__(self, key, value):
        for list_element in self._storage[self._compute_index(key)]:
            if key == list_element[0]:  # already exist, update its value
                list_element[1] = value
                break
        else:
            self._storage[self._compute_index(key)].append([key, value])
            self._length += 1

    def put(self, key, value):
        self.__setitem__(key, value)

    def _compute_index(self, key):
        return hash(key) % self._size

    def __getitem__(self, key):
        """
        get by key, if not found, raise key error
        :raise: KeyError
        :return: value
        """
        storage_idx = hash(key) % self._size
        for ele in self._storage[storage_idx]:
            if ele[0] == key:
                return ele[1]

        raise KeyError('Key {} dont exist'.format(key))

    def __delitem__(self, key):
        """
        delete key value from current dictionary instance
        :param key: str
        :return: None
        """
        storage_idx = hash(key) % self._size
        for sub_lst in self._storage[storage_idx]:
            if key == sub_lst[0]:
                self._storage[storage_idx].remove(sub_lst)
                self._length -= 1
                return

        raise KeyError('Key {} dont exist'.format(key))

    def __contains__(self, key):
        storage_index = hash(key) % self._size
        for item in self._storage[storage_index]:
            if item[0] == key:
                return True
        return False

    def __len__(self):
        return self._length

    def __iterate_kv(self):
        """
        return an iterator
        :return: generator
        """
        for sub_lst in self._storage:
            if not sub_lst:
                continue
            for item in sub_lst:
                yield item

    def __iter__(self):
        """
        return an iterator
        :return: generator
        """
        for key_var in self.__iterate_kv():
            yield key_var[0]

    def keys(self):
        """
        get all keys as list
        :return: list
        """
        return self.__iter__()

    def values(self):
        """
        get all values as list
        :return: list
        """
        for key_var in self.__iterate_kv():
            yield key_var[1]

    def items(self):
        """
        get all k:v as list
        :return: list
        """
        return self.__iterate_kv()

    def get(self, key):
        """
        get value by key
        :param key: str
        :return: value
        """
        try:
            return self.__getitem__(key)
        except KeyError:
            return None

    def __str__(self):
        """
        str representation of the dictionary
        :return: string
        """
        res = []
        for ele in self._storage:
            for key_value in ele:
                if isinstance(key_value[0], str):
                    key_str = '\'{}\''.format(key_value[0])
                else:
                    key_str = '{}'.format(key_value[0])
                if isinstance(key_value[1], str):
                    value_str = '\'{}\''.format(key_value[1])
                else:
                    value_str = '{}'.format(key_value[1])

                res.append('{}: {}'.format(key_str, value_str))
        key_value_pairs_str = '{}'.format(', '.join(res))
        return '{' + key_value_pairs_str + '}'

    def __repr__(self):
        """
        string representation of the class instances
        :return: string
        """
        return self.__str__()


dic = HashTable()
dic[1] = 2
dic[3] = "Anna"
dic["age"] = 10
dic.__setitem__("available", True)


print(dic)




