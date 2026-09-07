class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0

        prefix_sums = [0] * len(nums)
        cur_prefix_sum = 0
        for i in range(len(nums)):
            prefix_sums[i] = cur_prefix_sum
            cur_prefix_sum += nums[i]
        
        total = cur_prefix_sum
        
        valid_postfix_sums = defaultdict(int)
        valid_postfix_sums[0] = 1

        cur_postfix_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            postfix_needed = total - prefix_sums[i] - k
            res += valid_postfix_sums[postfix_needed]

            cur_postfix_sum += nums[i]
            valid_postfix_sums[cur_postfix_sum] += 1
        
        return res