class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]

                if abs(target-total) < abs(target-res):
                    res = total
                if total == target:
                    return target
                elif total < target:
                    l +=1
                else:
                    r-=1
        return res

        