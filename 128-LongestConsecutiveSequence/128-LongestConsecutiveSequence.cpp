// Last updated: 10/08/2026, 02:36:13
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;  // handle empty case
        
        int n = nums.size();
        int count = 1;
        int maxCount = 1;
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n - 1; i++) {
            // If the next element is a duplicate, continue without resetting or increasing the count
            if (nums[i] == nums[i+1]) continue;
            
            if (nums[i] + 1 == nums[i+1]) {
                count++;
                maxCount = max(maxCount, count);
            } else {
                count = 1;  // Reset to 1 because the next number is the start of a new sequence
            }
        }
        return maxCount;
    }
};
