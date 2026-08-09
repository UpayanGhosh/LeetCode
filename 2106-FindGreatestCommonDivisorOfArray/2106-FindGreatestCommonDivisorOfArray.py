# Last updated: 10/08/2026, 02:33:42
class Solution(object):
    def findGCD(self, nums):
        sorted_nums = nums.sort()
        smallNumber = nums[0]
        largeNumber = nums[-1]
        for i in range(1, smallNumber + 1):
            if((smallNumber % i == 0) and (largeNumber % i == 0)):
                HCF = i
        return HCF
        