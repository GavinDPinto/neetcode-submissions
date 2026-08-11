class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnts = defaultdict(int)
        s1_len = 0
        for c in s1:
            s1_cnts[c] += 1
            s1_len += 1
        
        window_cnts = defaultdict(int)
        window_len = 0
        left = 0
        for right, c in enumerate(s2):
            window_len += 1
            window_cnts[c] += 1
            while window_cnts[c] > s1_cnts[c]:
                window_cnts[s2[left]] -= 1
                left += 1
                window_len -= 1
            if window_len == s1_len: return True
        
        return False