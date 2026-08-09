# Last updated: 10/08/2026, 02:37:11
class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the array to apply two-pointer technique
        res = []  # This will store the list of unique triplets

        for i in range(len(nums)):
            # Skip duplicate values for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers: left and right
            left = i + 1
            right = len(nums) - 1

            # While there's a valid range between left and right
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Calculate the current sum of triplet

                if total == 0:
                    # If a valid triplet is found, add it to the result
                    res.append((nums[i], nums[left], nums[right]))

                    # Skip duplicates for the second element of the triplet
                    while left < right and nums[left] == nums[left + 1]: 
                        left += 1

                    # Skip duplicates for the third element of the triplet
                    while left < right and nums[right] == nums[right - 1]: 
                        right -= 1

                    # Move both pointers inward after recording the triplet
                    left += 1
                    right -= 1

                elif total < 0:
                    # If sum is less than 0, move left pointer to the right to increase the total
                    left += 1
                elif total > 0:
                    # If sum is more than 0, move right pointer to the left to decrease the total
                    right -= 1

        return res  # Return all unique triplets that sum to 0
