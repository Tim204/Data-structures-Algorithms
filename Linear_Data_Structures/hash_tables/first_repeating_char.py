""" Finding the First Non-Repeating Character on a string using
    Hash-tables(Dictionaries)"""


class CharFinder:
    def __init__(self):
        self._dict = {}

    def non_repeating_chars(self, string):
        for chars in string.lower():
            if chars.isalpha():
                self._dict.__setitem__(chars, string.lower().count(chars))

        for key, value in self._dict.items():
            if value == 1:
                return key
        return 0


ch = CharFinder()
print(ch.non_repeating_chars("I Live off Grid"))
