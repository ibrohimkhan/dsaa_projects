from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

    def suffixes(self, suffix=''):
        found_suffix = []

        for char, node in self.children.items():
            if node.is_word:
                found_suffix.append(suffix + char)
            if node.children:
                found_suffix += node.suffixes(suffix + char)

        return found_suffix


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]

        return current_node

    def exists(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word


def tests():
    trie = Trie()

    word_list = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]

    for word in word_list:
        trie.insert(word)

    # Find
    assert type(trie.find("a")) is TrieNode
    assert trie.find("A") is None

    # Exists
    assert trie.exists("ant") is True
    assert trie.exists("tripod") is True
    assert trie.exists("anthony") is False
    assert trie.exists("hi") is False

    # Suffixes
    node = trie.find("a")
    assert node.suffixes() == ["nt", "nthology", "ntagonist", "ntonym"]

    node = trie.find("")
    assert node.suffixes() == [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]

    node = trie.find("fact")
    assert node.suffixes() == ["ory"]

    node = trie.find("function")
    assert node.suffixes() == []


if __name__ == '__main__':
    tests()
