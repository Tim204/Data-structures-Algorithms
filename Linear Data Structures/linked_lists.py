
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def add_first(self, item):
        node = Node(item)

        if self._first is None:
            self._first = self._last = node
        else:
            # Set node to point to the first node
            node.next = self._first
            self._first = node
        # Increment size to keep track of count of items added
        self._size += 1

    def add_last(self, item):
        node = Node(item)

        if self._first is None:
            # Set first and last to node
            self._first = self._last = node
        else:
            # Add a node after the last node
            self._last.next = node
            # update last node to point to the new node
            self._last = node
        self._size += 1

    def remove_first(self):
        if self._first is None:
            return Exception("The list is empty")
        else:
            second = self._first.next
            self._first = None
            self._first = second
        self._size -= 1

    def remove_last(self):
        if self._first is None:
            return Exception("The list is empty")
        if self._first == self._last:
            self._first = self._last = None
        else:
            previous_node = self._get_previous(self._last)
            self._last = previous_node
            self._last.next = None
        self._size -= 1

    def index_of(self, item):
        index = 0
        current = self._first

        while current is not None:
            if current.value == item:
                return index
            current = current.next
            index += 1
        return -1

    def sizeof(self):
        return self._size

    def contains(self, item):
        # Reusing index_of logic to check for the existence of an item to avoid repetition.
        return self.index_of(item) != -1

    def convert_to_list(self):
        array = []
        current = self._first
        while current:
            array.append(current.value)
            current = current.next
        return array

    def _get_previous(self, node):
        current = self._first

        while current is not None:
            if current.next == node:
                return current
            else:
                current = current.next

    def reverse(self):
        previous = None
        current = self._first

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self._first = previous

    def get_kth_from_end(self, k):
        a = self._first
        b = self._first
        count = 0
        while count < k-1:
            if b is None:
                raise Exception("Value error")
            else:
                b = b.next
                count += 1

        while b != self._last:
            a = a.next
            b = b.next
        return a.value

    def print_lis(self):
        first_node = self._first
        while first_node:
            print(first_node.value)
            first_node = first_node.next


week_days = LinkedList()

week_days.add_last("Monday")
week_days.add_last("Wednesday")
week_days.add_last("Friday")
week_days.add_first("Sunday")




print(week_days.sizeof())
print(week_days.convert_to_list())
print(week_days.convert_to_list())

print(week_days.get_kth_from_end(0))

# sl.add_first(25)
#
# print(sl.sizeof())
# sl.print_lis()
# sl.remove_last()
# print(sl.sizeof())
