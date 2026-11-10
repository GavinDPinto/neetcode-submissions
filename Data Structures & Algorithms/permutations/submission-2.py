class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        perm = []
        chosen = [False] * len(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not chosen[i]:
                    perm.append(nums[i])
                    chosen[i] = True
                    dfs()
                    perm.pop()
                    chosen[i] = False
        
        dfs()
        return res