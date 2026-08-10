class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2: return len(s)
        
        maxf = 0 # all-time max frequency of a letter in any valid window
        freqs = [0] * 26
        left, right = 0, 0

        c = s[right]
        freqs[ord(c)-ord('A')] += 1
        cur_freq = freqs[ord(c)-ord('A')]
        maxf = max(cur_freq, maxf)

        while right < len(s) - 1:
            if 1+right-left - maxf > k:
                freqs[ord(s[left])-ord('A')] -= 1
                left += 1
            else:
                right += 1
                c = s[right]
                freqs[ord(c)-ord('A')] += 1
                cur_freq = freqs[ord(c)-ord('A')]
                maxf = max(cur_freq, maxf)
        
        return min(len(s), maxf+k)
