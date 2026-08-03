class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s) - 1
        while front < back:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[back].isalnum():
                back -= 1
                continue
            l_char = s[front].lower()
            r_char = s[back].lower()
            if l_char != r_char:
                return False
            front += 1
            back -= 1
        return True
            