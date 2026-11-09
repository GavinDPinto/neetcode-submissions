class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if cur.children[ord(ch) - ord('a')] is None:
                cur.children[ord(ch) - ord('a')] = TrieNode()
            cur = cur.children[ord(ch) - ord('a')]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if cur.children[ord(ch) - ord('a')] is None:
                return False
            cur = cur.children[ord(ch) - ord('a')]
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if cur.children[ord(ch) - ord('a')] is None:
                return False
            cur = cur.children[ord(ch) - ord('a')]
        return True
        
        