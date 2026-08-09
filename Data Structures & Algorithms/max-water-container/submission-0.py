class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        l, r = 0, len(heights) - 1

        while l < r:
            volume = (r-l) * min(heights[l], heights[r])
            max_volume = max(max_volume, volume)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_volume