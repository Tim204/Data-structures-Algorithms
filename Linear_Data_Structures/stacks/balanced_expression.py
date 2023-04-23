from stacks import Stack

"""Common interview type question that can be solved using stacks"""


class Expression:
    def __init__(self):
        self.stack = Stack()
        self._left_brackets = ("(", "<", "[", "{")
        self._right_brackets = (")", ">", "]", "}")

    def is_balanced(self, input_string):
        for char in input_string:
            if self._is_left_bracket(char):
                self.stack.push(char)
            if self._is_right_bracket(char):
                if self.stack.is_empty():
                    return False
                top = self.stack.pop()
                if not self._brackets_match(top, char):
                    return False
        return self.stack.is_empty()

    def _is_left_bracket(self, char):
        return self._left_brackets.__contains__(char)

    def _is_right_bracket(self, char):
        return self._right_brackets.__contains__(char)

    def _brackets_match(self, left, right):
        return self._left_brackets.index(left) == self._right_brackets.index(right)


exp = Expression()
print(exp.is_balanced("<><1+2()()"))

