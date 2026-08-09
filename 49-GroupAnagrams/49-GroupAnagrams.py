# Last updated: 10/08/2026, 02:36:49
from collections import Counter, defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for words in strs:
            key = frozenset(Counter(words).items())
            groups[key].append(words)
        return list(groups.values())
        