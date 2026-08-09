// Last updated: 10/08/2026, 02:36:42
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int currSum = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            // Either add nums[i] to current sum or start a new subarray from nums[i]
            currSum = max(nums[i], currSum + nums[i]);
            maxSum = max(maxSum, currSum);
        }
        
        return maxSum;
    }
};
