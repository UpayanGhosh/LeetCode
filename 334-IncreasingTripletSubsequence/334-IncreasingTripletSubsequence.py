# Last updated: 10/08/2026, 02:35:14
class Solution(object):
    def increasingTriplet(self, nums):
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
        