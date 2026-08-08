class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums
        self.heapsort(nums)
        print(nums)
        ret = []
        # Solve twoSum where target = nums[i] and numbers = nums[i+1:] for each i and add the triplet of indices to ret
        i = 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ret.append((nums[i], nums[j], nums[k]))
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    k -= 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
            i += 1
            while nums[i] == nums[i-1] and i < len(nums) - 1:
                i += 1
                
        return ret
    
    def heapsort(self, nums):
        # Max-heapify (will make it so it sorts in ascending order)
        for i in range(len(nums)):
            cur_idx = i
            while cur_idx > 0 and nums[cur_idx] > nums[(cur_idx - 1) // 2]:
                nums[cur_idx], nums[(cur_idx - 1) // 2] = nums[(cur_idx - 1) // 2], nums[cur_idx]
                cur_idx = (cur_idx - 1) // 2
        
        # Sort by repeated popping
        for i in range(len(nums) - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            cur_idx = 0
            stop = 0
            while stop == 0:
                if (cur_idx * 2 + 2 < i and nums[cur_idx * 2 + 2] > nums[cur_idx] and nums[cur_idx * 2 + 2] > nums[cur_idx * 2 + 1]):
                    nums[cur_idx], nums[cur_idx * 2 + 2] = nums[cur_idx * 2 + 2], nums[cur_idx]
                    cur_idx = cur_idx * 2 + 2
                elif (cur_idx * 2 + 1 < i and nums[cur_idx * 2 + 1] > nums[cur_idx]):
                    nums[cur_idx], nums[cur_idx * 2 + 1] = nums[cur_idx * 2 + 1], nums[cur_idx]
                    cur_idx = cur_idx * 2 + 1
                else:
                    stop = 1
        


            