class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = len(nums) - 1
            k = i+1

            while k < j:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum == 0:
                        res.append([nums[i],nums[j],nums[k]])
                        k+=1
                        while k < j and nums[k] == nums[k-1]:
                            k += 1
                elif total_sum > 0:
                    j -= 1
                else:
                    k += 1
        return res





        