class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if cur.children[ord(ch) - ord('a')] is None:
                cur.children[ord(ch) - ord('a')] = TrieNode()
            cur = cur.children[ord(ch) - ord('a')]
        cur.endOfWord = True
            
        

    def search(self, word: str) -> bool:
        
        def dfs(index, node) -> bool:
            if index == len(word):
                return node.endOfWord

            c = word[index]
            if c == '.':
                # Try every existing child for the wildcard
                for child in node.children:
                    if child is not None and dfs(index + 1, child):
                        return True
                return False

            if node.children[ord(c) - ord('a')] is None:
                return False
            return dfs(index + 1, node.children[ord(c) - ord('a')])

        return dfs(0, self.root)
            
        
