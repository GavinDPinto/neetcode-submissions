class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(idx, path, total):
            if total == target:
                res.append(path)
                return
            if total > target or idx == len(nums):
                return
            
            # Choice 1: Include nums[idx] (can reuse the same element, hence pass idx)
            dfs(idx, path + [nums[idx]], total + nums[idx])
            
            # Choice 2: Exclude nums[idx] and move to the next element (idx + 1)
            dfs(idx + 1, path, total)

        dfs(0, [], 0)
        return res