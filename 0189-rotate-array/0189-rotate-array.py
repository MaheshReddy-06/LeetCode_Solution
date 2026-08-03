class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            last_ele = nums.pop()
            nums.insert(0,last_ele)

        