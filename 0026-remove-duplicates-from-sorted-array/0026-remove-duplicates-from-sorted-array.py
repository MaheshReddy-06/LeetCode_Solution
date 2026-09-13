class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        unique = {}
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique[nums[i]] = 0
        j = 0
        for k in unique:
            nums[j] = k
            j += 1
        return j
            
        

        