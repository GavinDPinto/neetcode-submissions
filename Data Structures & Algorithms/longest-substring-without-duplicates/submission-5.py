class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {} # past characters and their last location
        left = 0 
        for right, c in enumerate(s):
            if c in seen and seen[c] >= left: # check if new char is in the window
                res = max(res, right - left) # recalculate longest length
                left = seen[c] + 1 # move left boundary of window past the duplicate char
            seen[c] = right # update location
        res = max(res, len(s) - left)
        return res
