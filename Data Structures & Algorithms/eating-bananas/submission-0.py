class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end, k = 1, max(piles), max(piles)
        
        while start <= end:
            mid = (start + end) // 2
            acc = 0
            for pile in piles:
                acc += math.ceil(pile / mid)
            if acc <= h:
                k = mid
                end = mid - 1
            else:
                start = mid + 1
        
        return k