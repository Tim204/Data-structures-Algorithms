from stacks import Stack
"""One common interview question easily solved using stacks"""


class StringReverser:
    """Reversing a string using Stacks"""
    def __init__(self, string):
        self._string = string

    def reverse(self):
        reversed_string = ""
        stack = Stack()
        for char in self._string:
            stack.push(char)
        while not stack.is_empty():
            reversed_string += stack.pop()
        return reversed_string


class Reverse:
    """Reversing a string without using the use of stacks"""
    def __init__(self, string=""):
        self._string = string

    def reverse_string(self):
        items = ""
        for i in self.get_index_list():
            items += self._string[i]
        return items

    def get_index_list(self):
        index = []
        for i in range(self.length()):
            index.append(i)
        index.reverse()
        return index

    def length(self):
        return len(self._string)


stack_reverser = StringReverser("123456")
normal_reverser = Reverse("123456")

print(stack_reverser.reverse())
print(normal_reverser.reverse_string())


