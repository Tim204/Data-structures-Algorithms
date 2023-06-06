
class TrieNode:

    def __init__(self, value=None):
        self.value = value
        self._children = {}
        self._is_end = False

    def has_child(self, ch):
        return self._children.__contains__(ch)

    def add_child(self, ch):
        self._children.__setitem__(ch, TrieNode(ch))

    def get_child(self, ch):
        return self._children.get(ch)

    def get_children(self):
        return self._children.values()

    def __str__(self):
        return f"value={self.value}"

    def __repr__(self):
        return self.__str__()


class Trie(TrieNode):
    def __init__(self):
        super().__init__()
        self._root = TrieNode(' ')

    def inset(self, word):
        current = self._root
        for ch in word:
            if not current.has_child(ch):
                current.add_child(ch)
            current = current.get_child(ch)
        current._is_end = True

    def contains(self, word):
        if word is None:
            return False

        current = self._root
        for ch in word:
            if not current.has_child(ch):
                return False
            current = current.get_child(ch)
        return current._is_end

    def traverse(self):
        self._traverse(self._root)

    def _traverse(self, root):
        # PRE-ORDER-TRAVERSAL:  Visit the root first
        print(root.value)
        for child in root.get_children():
            self._traverse(child)

        # POST-ORDER: Simply visit the children first
        # for child in root.get_children():
        #     self._traverse(child)
        # print(root.value)


trie = Trie()
trie.inset("compare")
trie.traverse()
print(trie.contains(None))
