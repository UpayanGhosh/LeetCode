# Last updated: 16/08/2026, 20:55:01
1class Solution(object):
2    def twoSum(self, numbers, target):
3        seen = {}
4        for i, num in enumerate(numbers):
5            if target - num in seen:
6                return [seen[target - num] + 1, i + 1]
7            else:
8                seen[num] = i
9        