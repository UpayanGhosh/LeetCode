# Last updated: 10/08/2026, 02:34:43
class Solution(object):
    def findMaxAverage(self, nums, k):
        total_sum = sum(nums[:k])  # Calculate the initial sum of the first k elements
        max_sum = total_sum

        for i in range(k, len(nums)):
            total_sum += nums[i] - nums[i - k]  # Update the total sum using a sliding window
            max_sum = max(max_sum, total_sum)

        return max_sum / float(k)
