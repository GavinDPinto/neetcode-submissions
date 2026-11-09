class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # note all nums positive

        res = []
        curcomb = []
        cursum = 0

        def dfs(idx):
            nonlocal cursum
            if cursum > target:
                return
            if cursum == target:
                res.append(curcomb.copy())
                return
            
            for i in range(len(nums[idx:])):
                # include n
                curcomb.append(nums[idx + i])
                cursum += nums[idx + i]
                dfs(i + idx)
                # don't include n
                curcomb.pop()
                cursum -= nums[idx + i]
        
        dfs(0)
        return res
