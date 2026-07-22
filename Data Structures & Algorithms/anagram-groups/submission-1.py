class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # a sample entry would be (1,1,0,2): ["dabd","addb"]

        # create the groups in a dict where
        # the key is the "representative tuple" and value is the list of strings in group
        for string in strs:
            # turn string like "badd" to tuple representative (TR) like (1,1,0,2)
            anagram_group = self.tuplify(string)
            # checks if TR exists as a key in the dict
            if anagram_group in groups:
                # if it does, it appends to the list already there so now its TR: ["dabd","addb", "badd"]
                groups[anagram_group].append(string)
            else:
                # if it doesnt already exist it forms a new group
                groups[anagram_group] = [string]

        # a big list of all the smaller lists 
        return [group for group in groups.values()]
    
    # turns a string from badd -> (1,1,0,2)
    def tuplify(self, string: str) -> tuple:
        alphabet = [0] * 26
        for letter in string:
            alphabet[ord(letter) - ord('a')] += 1
        return tuple(alphabet)
        
 
        

