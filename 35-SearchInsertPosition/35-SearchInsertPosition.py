# Last updated: 10/08/2026, 02:36:54
class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        elif target < nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        