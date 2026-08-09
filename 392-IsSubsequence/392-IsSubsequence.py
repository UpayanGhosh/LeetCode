# Last updated: 10/08/2026, 02:34:59
class Solution(object):
    def isSubsequence(self, s, t):
        iter_t = iter(t)
        if all(char in iter_t for char in s):
            return True
        else:
            return False
        
        