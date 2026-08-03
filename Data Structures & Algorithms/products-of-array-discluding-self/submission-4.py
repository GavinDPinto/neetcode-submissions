class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Build prefix array
        product = 1
        prefix_arr = [1] * len(nums)
        for i in range(len(nums)):
            prefix_arr[i] *= product
            product *= nums[i]
        
        # Build return array (prefix * suffix)
        product = 1
        ret = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            ret[i] = (product * prefix_arr[i])
            product *= nums[i]
        
        return ret