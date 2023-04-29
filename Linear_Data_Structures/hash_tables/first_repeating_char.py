"""
    Finding Repeating Character on a string using
    Hash-tables(Dictionaries) and sets
"""


class CharFinder:
    def __init__(self):
        self._dict = {}

    def first_non_repeating_chars(self, string):
        for char in string.lower():
            if char.isalpha():
                self._dict.__setitem__(char, string.lower().count(char))

        for key, value in self._dict.items():
            if value == 1:
                return key
        return None

    def first_repeating_char(self, string):
        """For getting the first repeating char a set can be used instead of a dict"""
        self._dict = {None}  # Passing None to the dict as key to trick the interpreter to think it's a set
        for char in string.lower():
            if self._dict.__contains__(char):
                return char
            self._dict.add(char.lower())
        return None


find = CharFinder()
print(find.first_non_repeating_chars("Hello world!"))
print(find.first_repeating_char("Hello world!"))
