class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curStr, opens, closes):
            if closes == n:
                res.append(curStr)
                return
            
            if opens < n:
                dfs(curStr + '(', opens + 1, closes)
            
            if closes < opens:
                dfs(curStr + ')', opens, closes + 1)
        
        dfs("", 0, 0)
        return res