class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            ret.extend([subset + [n] for subset in ret])
        return ret