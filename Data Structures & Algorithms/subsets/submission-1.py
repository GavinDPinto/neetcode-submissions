class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking soln
        res = []
        subset = []

        def dfs(idx):
            # idx is out of bounds; no more decisions
            if idx >= len(nums):
                res.append(subset.copy())
                return
            # decision 1: include nums[idx]
            subset.append(nums[idx])
            dfs(idx + 1)
            # decision 2: don't include nums[idx]
            subset.pop()
            dfs(idx + 1)
        
        dfs(0)
        return res