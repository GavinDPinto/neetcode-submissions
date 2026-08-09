class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}
        left = 0
        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                res = max(res, right - left)
                left = seen[c] + 1
            seen[c] = right
        res = max(res, len(s) - left)
        return res
