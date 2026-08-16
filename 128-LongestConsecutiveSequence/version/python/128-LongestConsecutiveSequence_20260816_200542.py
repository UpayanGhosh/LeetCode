# Last updated: 16/08/2026, 20:05:42
1class Solution(object):
2    def longestConsecutive(self, nums):
3        num_set = set(nums)
4        best = 0
5        for num in num_set:
6            if num - 1 not in num_set:
7                length = 1
8                while num + length in num_set:
9                    length += 1
10                best = max(best , length)
11        return best
12        