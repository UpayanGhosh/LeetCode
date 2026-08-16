# Last updated: 16/08/2026, 20:16:03
1class Solution(object):
2    def isPalindrome(self, s):
3        cleaned = [c.lower() for c in s if c.isalnum()]
4        return cleaned == cleaned[:: -1]
5        