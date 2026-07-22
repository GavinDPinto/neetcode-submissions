class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for index, num in enumerate(nums):
            if (target - num) in visited:
                return [visited[target - num], index]
            else:
                visited[num] = index
        return [-1,-1] # never reaches here