class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def dfs(idx, path):
            if idx == len(digits):
                res.append(path)
                return
            for letter in map[int(digits[idx])]:
                dfs(idx + 1, path + letter)
        
        dfs(0, "")
        return res if digits else []