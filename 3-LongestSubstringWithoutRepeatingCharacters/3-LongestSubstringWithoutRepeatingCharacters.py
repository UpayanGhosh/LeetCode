# Last updated: 10/08/2026, 02:37:29
import collections
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res




        