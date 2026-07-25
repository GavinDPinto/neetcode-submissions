class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # determine frequency of the elements
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        n = len(nums)

        # put elements into buckets where bucket i has the elements with i+1 freq 
        buckets = [[] for _ in range(n)]
        for num in counts.keys():
            buckets[counts[num] - 1].append(num)
        
        ret = []
        i = n - 1 # representing index of bucket list
        # take first k elements from highest buckets and add to ret
        while k > 0:
            nsub = len(buckets[i])
            if nsub <= k:
                ret.extend(buckets[i])
                k -= nsub
            else:
                ret.extend(buckets[i][:k])
            i -= 1
        
        return ret