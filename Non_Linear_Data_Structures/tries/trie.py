
class TrieNode:

    def __init__(self, value=None):
        self.value = value
        self._children = {}
        self._is_end = False

    def has_child(self, ch):
        return self._children.__contains__(ch)

    def has_children(self):
        return not len(self._children) == 0

    def add_child(self, ch):
        self._children.__setitem__(ch, TrieNode(ch))

    def get_child(self, ch):
        return self._children.get(ch)

    def get_children(self):
        return self._children.values()

    def remove_child(self, ch):
        self._children.pop(ch)

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

    def remove(self, word):
        if word is None:
            return
        self._remove(self._root, word, 0)

    def _remove(self, root, word, index):
        if index == len(word):
            # Remove the end of the word marker
            root._is_end = False
            return

        ch = word[index]
        child = root.get_child(ch)
        if child is None:
            return

        self._remove(child, word, index + 1)
        if not child.has_children() and not child._is_end:
            root.remove_child(ch)

    def find_words(self, prefix):
        words = []
        last_node = self.find_last_node(prefix)
        self._find_words(last_node, prefix, words)
        return words

    def _find_words(self, root, prefix, words):
        if root is None:
            return
        if root._is_end:
            words.append(prefix)

        for child in root.get_children():
            self._find_words(child, prefix + child.value, words)

    def find_last_node(self, prefix):
        if prefix is None:
            return
        current = self._root
        for ch in prefix:
            child = current.get_child(ch)
            if child is None:
                return None
            current = child
        return current


trie = Trie()
trie.inset("car")
trie.inset("card")
trie.inset("care")
trie.inset("careful")
trie.inset("carefully")
trie.inset('egg')

print(trie.find_words('care'))
print(trie.find_words('e'))

