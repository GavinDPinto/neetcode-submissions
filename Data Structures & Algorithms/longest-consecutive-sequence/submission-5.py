class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unvisited = set(nums)
        # maps beginning of sequence to its length
        seqs = defaultdict(int)
        longest_seq = 0
        while len(unvisited):
            elem =  unvisited.pop()
            seq_len = 1
            next = elem + 1
            while next in unvisited:
                unvisited.remove(next)
                seq_len += 1
                next += 1
            # add length of (seq starting with next value not there), otherwise 0
            seq_len += seqs[next]
            longest_seq = max(seq_len, longest_seq)
            # set length of seq starting with orig elem
            seqs[elem] = seq_len
        return longest_seq

