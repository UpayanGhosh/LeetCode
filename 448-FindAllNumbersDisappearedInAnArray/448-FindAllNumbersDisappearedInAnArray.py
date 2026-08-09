# Last updated: 10/08/2026, 02:34:56
class Solution(object):
    def findDisappearedNumbers(self, nums):
        res = []
        set_nums = set(nums)
        for i in range(1,len(nums) + 1):
            if i not in set_nums:
                res.append(i)
        return res