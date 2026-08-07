class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 1, len(numbers)

        while left < right:
            leftnum = numbers[left - 1]
            rightnum = numbers[right - 1]
            sumM = leftnum + rightnum
            if sumM == target:
                return [left, right]
            elif sumM < target:
                left += 1
            elif sumM > target:
                right -= 1
        
        return [-1, -1]