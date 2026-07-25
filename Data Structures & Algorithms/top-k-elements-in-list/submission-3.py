class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        n = len(nums)
        buckets = [[] for _ in range(n)]
        for num in counts.keys():
            buckets[counts[num] - 1].append(num)
        
        ret = []
        i = len(nums) - 1
        while k > 0:
            nsub = len(buckets[i])
            if nsub <= k:
                ret.extend(buckets[i])
                k -= nsub
            else:
                ret.extend(buckets[i][:k])
            i -= 1

        return ret