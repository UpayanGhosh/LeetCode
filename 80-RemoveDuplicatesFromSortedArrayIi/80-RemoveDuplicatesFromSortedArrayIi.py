# Last updated: 10/08/2026, 02:36:23
class Solution(object):
    def removeDuplicates(self, nums):
        s = set(nums)
        for i in set(s):
            while nums.count(i) > 2:
                nums.remove(i)
        return len(nums)
        