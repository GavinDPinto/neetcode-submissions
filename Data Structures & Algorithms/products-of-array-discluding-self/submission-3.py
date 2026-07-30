class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Naive solution - O(n) time with division operation
        # Depends on # of zeros
        # No zeros: take product of all and divide by each num
        # 1 zero: take product of remaining
        # 2+ zeros: everything 0

        zero_count = 0
        product_nums = 1
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count > 1:
                    return [0] * len(nums)
            else:
                product_nums *= num
        
        ret = []
        for i in range(len(nums)):
            if nums[i] == 0:
                ret.append(product_nums)
            elif zero_count == 1:
                ret.append(0)
            else:
                ret.append(product_nums // nums[i])
         
        return ret

            
        