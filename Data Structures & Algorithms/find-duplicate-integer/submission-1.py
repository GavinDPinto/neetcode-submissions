class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i + 1:
                continue
            while nums[i] != i + 1:
                temp = nums[i]
                if temp == nums[temp - 1]:
                    return temp
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        return -1


