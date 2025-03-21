from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str, index: int, count: int) -> bool:
        node = self.root
        for i in range(index, len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            if node.is_end:
                if i == len(word) - 1:
                    return count >= 1
                if self.search(word, i + 1, count + 1):
                    return True
        return False

def findAllConcatenatedWords(words: List[str]) -> List[str]:
    words = sorted(words, key=len)  # Sort words by length
    trie = Trie()
    result = []

    for word in words:
        if word and trie.search(word, 0, 0):
            result.append(word)
        trie.insert(word)

    return result

# Example test
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWords(words))  # Output: ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
