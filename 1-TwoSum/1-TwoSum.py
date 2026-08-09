# Last updated: 10/08/2026, 02:37:33
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target - num], i]
            else:
                seen[num] = i
        