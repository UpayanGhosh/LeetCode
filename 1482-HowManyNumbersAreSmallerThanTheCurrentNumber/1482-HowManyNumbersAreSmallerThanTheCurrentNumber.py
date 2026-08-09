# Last updated: 10/08/2026, 02:34:05
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        tempArray = nums[:]
        sorted_nums = sorted(nums)
        hashMap = {}
        for key,value in enumerate(sorted_nums):
            if value not in hashMap:
                hashMap[value] = key
        ans = []
        for i in tempArray:
            ans.append(hashMap[i])
        return ans

