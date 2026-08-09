# Last updated: 10/08/2026, 02:35:24
class Solution(object):
    def missingNumber(self, nums):
        totalSum = sum(nums)
        n = len(nums)
        Sum = (n * (n + 1))/2
        return Sum - totalSum
        