# Last updated: 10/08/2026, 02:37:23
class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)
        reverse = x_str[::-1]
        if str(x) == reverse:
            return True
        else:
            return False
        