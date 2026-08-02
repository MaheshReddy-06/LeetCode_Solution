class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        n = len(nums)
        count = 0
        for k in range(n):
            rotated = sorted_nums[k:] + sorted_nums[:k]
            if rotated == nums:
                return True

        return False
        
        