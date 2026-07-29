class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        max_count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
            else:
                max_count = max(max_count, r - l + 1)
        return max_count
