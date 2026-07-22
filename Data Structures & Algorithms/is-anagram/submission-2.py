class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = [0] * 26
        for letter in s:
            alphabet[ord(letter) - ord('a')] += 1
        for letter in t:
            alphabet[ord(letter) - ord('a')] -= 1
        for count in alphabet:
            if count != 0:
                return False
        return True