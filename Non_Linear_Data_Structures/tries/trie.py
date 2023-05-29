class Node:

    def __init__(self, value=None, length=26):
        self._value = value
        self._children = [length]
        self._is_end = False

    def __str__(self):
        return f"value={self._value}"


class Trie(Node):
    def __init__(self):
        super().__init__()
        self._root = Node(' ')

    def inset(self, word):
        current = self._root
        for ch in word:
            index = ord(ch) - ord("a")


        current._is_end = True


trie = Trie()
trie.inset("cat")
trie.inset("can")
print("Done")