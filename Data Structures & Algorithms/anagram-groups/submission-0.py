class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        groups = {}

        # create the groups in a dict where
        # the key is the "representative tuple" and value is the list of strings in group
        for string in strs:
            anagram_group = self.tuplify(string)
            if anagram_group in groups:
                groups[anagram_group].append(string)
            else:
                groups[anagram_group] = [string]

        return [group for group in groups.values()]
    
    def tuplify(self, string: str) -> str:
        alphabet = [0] * 26
        for letter in string:
            alphabet[ord(letter) - ord('a')] += 1
        return tuple(alphabet)
        

        

