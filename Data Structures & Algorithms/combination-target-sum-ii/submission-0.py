class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, path, total):
            if total == target:
                res.append(path.copy())
                return
            if idx >= len(candidates) or total > target:
                return
            
            # 1) add candidates[idx]
            dfs(idx + 1, path + [candidates[idx]], total + candidates[idx])

            # 2) dont add, but skip past any numbers of same value
            idx += 1
            while idx < len(candidates) and candidates[idx] == candidates[idx - 1]:
                idx += 1
            dfs(idx, path, total)
        
        dfs(0, [], 0)
        return res
                