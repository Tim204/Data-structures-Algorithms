""" Finding the First Non-Repeating Character on a string using
    Hash-tables(Dictionaries)"""


class CharFinder:
    def __init__(self):
        self._dict = {}

    def non_repeating_chars(self, string):
        for chars in string:
            if chars.isalpha():
                self._dict[chars.lower()] = string.count(chars)

        for key, value in self._dict.items():
            if value == 1:
                return key
            return 0


ch = CharFinder()
print(ch.non_repeating_chars("hello world"))





