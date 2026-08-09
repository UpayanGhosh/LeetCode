# Last updated: 10/08/2026, 02:34:18
class Solution(object):
    def sortedSquares(self, nums):
        # Square each number and create a new list
        squared = [x * x for x in nums]
        # Sort the squared values
        squared.sort()
        return squared