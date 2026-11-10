class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        def dfs(i, j, word):
            if not word:
                return True
            if (i, j) in visited or i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
                return False
            
            visited.add((i, j))
            res1, res2, res3, res4 = dfs(i - 1, j, word[1:]), dfs(i + 1, j, word[1:]), dfs(i, j - 1, word[1:]), dfs(i, j + 1, word[1:])
            visited.remove((i, j))

            return res1 or res2 or res3 or res4
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True
        
        return False
            
