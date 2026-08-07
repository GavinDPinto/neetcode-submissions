class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)

        while left < right:
            leftnum = numbers[left - 1]
            rightnum = numbers[right - 1]
            sum = leftnum + rightnum
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        
        return [-1, -1]