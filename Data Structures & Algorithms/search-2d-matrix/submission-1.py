class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.m, self.n = len(matrix), len(matrix[0])
        start, end = 0, self.getk(self.m - 1, self.n - 1)

        while start <= end:
            mid = (start + end) // 2
            if matrix[self.getrow(mid)][self.getcol(mid)] == target:
                return True
            elif matrix[self.getrow(mid)][self.getcol(mid)] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False
            

    def getrow(self, k):
        return k // self.n

    def getcol(self, k):
        return k % self.n
    
    def getk(self, i, j):
        return i * self.n + j