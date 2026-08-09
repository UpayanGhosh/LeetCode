# Last updated: 10/08/2026, 02:33:55
class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        ans = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            curr = nums[l] + nums[r]
            if curr == k:
                ans += 1
                l += 1
                r -= 1
            elif curr < k:
                l += 1
            else:
                r -= 1
        return ans
        