class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            x = nums[i]
            sum = 0

            while x > 0:
                sum += x%10
                x//=10
                
            if sum == i:
                return i
        return -1