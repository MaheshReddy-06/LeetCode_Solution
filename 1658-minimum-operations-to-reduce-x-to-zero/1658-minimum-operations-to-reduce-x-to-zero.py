class Solution:
    def minOperations(self, nums, x):
        n = len(nums)
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        if target == 0:
            return n

        l = 0
        s = 0
        longest = -1
        for r in range(n):
            s += nums[r]
            while l <= r and s > target:
                s -= nums[l]
                l += 1
            if s == target:
                longest = max(longest, r - l + 1)

        return -1 if longest == -1 else n - longest   