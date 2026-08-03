class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unvisited = set(nums)
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
            seq_len += seqs[next]
            longest_seq = max(seq_len, longest_seq)
            seqs[elem] = seq_len
        return longest_seq

