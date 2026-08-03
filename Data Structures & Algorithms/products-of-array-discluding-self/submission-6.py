class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Build prefix array
        l_product = 1
        prefix_arr = [1] * len(nums)
        for i in range(len(nums)):
            prefix_arr[i] *= l_product
            l_product *= nums[i]
        
        # Build return array (prefix * suffix)
        r_product = 1
        ret = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            ret[i] = (r_product * prefix_arr[i])
            r_product *= nums[i]
        
        return ret