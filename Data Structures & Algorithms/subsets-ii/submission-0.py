class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(idx, subset):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            # add nums[idx]
            dfs(idx + 1, subset + [nums[idx]])

            # dont add nums[idx] + skip future numbers with same value
            idx += 1
            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1
            dfs(idx, subset)
        
        dfs(0, [])
        return res