# Last updated: 16/08/2026, 17:27:10
1class Solution(object):
2    def groupAnagrams(self, strs):
3        groups = collections.defaultdict(list)
4        for words in strs:
5            key = frozenset(collections.Counter(words).items())
6            groups[key].append(words)
7        return list(groups.values())
8        