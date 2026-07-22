class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for index, num in enumerate(nums):
            potential_i = visited.get(target - num)
            if potential_i is not None:
                return [potential_i, index]
            else:
                visited[num] = index
        return [-1,-1] # never reaches here