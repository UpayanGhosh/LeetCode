# Last updated: 10/08/2026, 02:35:05
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        return [num for num, freq in Counter(nums).most_common(k)]
        