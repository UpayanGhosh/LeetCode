# Last updated: 10/08/2026, 02:35:26
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
        