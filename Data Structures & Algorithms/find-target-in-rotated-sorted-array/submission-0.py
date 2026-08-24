class Solution:
    def search(self, nums: List[int], target: int) -> int:
        offset = self.findMinIndex(nums)
        
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[(mid + offset) % len(nums)] == target:
                return (mid + offset) % len(nums)
            elif nums[(mid + offset) % len(nums)] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
    
    
    def findMinIndex(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[start] < nums[end]:
                return start
            elif start == mid:
                return end
            elif nums[start] < nums[mid]:
                start = mid
            else:
                end = mid
        return start
        