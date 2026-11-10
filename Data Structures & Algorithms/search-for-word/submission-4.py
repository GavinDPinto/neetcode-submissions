class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        L = len(word)
        def dfs(i, j, word_pos):
            if word_pos == L:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[word_pos]:
                return False
            
            board[i][j] = "#"
            res1, res2, res3, res4 = dfs(i - 1, j, word_pos + 1), dfs(i + 1, j, word_pos + 1), dfs(i, j - 1, word_pos + 1), dfs(i, j + 1, word_pos + 1)
            board[i][j] = word[word_pos]

            return res1 or res2 or res3 or res4
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
            
