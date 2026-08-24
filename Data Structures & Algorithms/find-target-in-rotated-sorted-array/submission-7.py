class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1 pass O(logn) solution
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[start] <= nums[mid]: # left half sorted
                if nums[start] <= target and target <= nums[mid]: # target in lower half
                    end = mid - 1 # search left
                else:
                    start = mid + 1 # search right
            else: # right half sorted
                if nums[mid] <= target and target <= nums[end]: # target in upper half
                    start = mid + 1 # search right
                else:
                    end = mid - 1 # search left
        return -1