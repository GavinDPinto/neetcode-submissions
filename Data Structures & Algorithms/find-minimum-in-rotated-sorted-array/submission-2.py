class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[start] < nums[end]:
                return nums[start]
            elif start == mid:
                return nums[end]
            elif nums[start] < nums[mid]:
                start = mid
            else:
                end = mid
        return nums[start]