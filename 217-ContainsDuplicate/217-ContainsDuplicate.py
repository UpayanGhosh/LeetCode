# Last updated: 10/08/2026, 02:35:43
class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return True
            else:
                seen[num] = i
        return False
        