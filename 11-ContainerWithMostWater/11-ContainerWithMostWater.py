# Last updated: 10/08/2026, 02:37:21
class Solution(object):
    def maxArea(self, height):
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res,area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
        