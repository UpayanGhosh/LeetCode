// Last updated: 10/08/2026, 02:35:23
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int j = 0; // pointer for placing non-zero elements

        // Move non-zero elements forward.
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[j++] = nums[i];
            }
        }

        // Fill the rest with zeroes.
        while (j < n) {
            nums[j++] = 0;
        }
    }
};
