# Last updated: 16/08/2026, 18:33:28
1class Solution(object):
2    def productExceptSelf(self, nums):
3        res = [1] * len(nums)
4        prefix = 1
5        for i in range(len(nums)):
6            res[i] = prefix
7            prefix *= nums[i]
8        postfix = 1
9        for i in range(len(nums) -1 , -1, -1):
10            res[i] *= postfix
11            postfix *= nums[i]
12        return res
13        