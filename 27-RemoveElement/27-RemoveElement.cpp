// Last updated: 10/08/2026, 02:37:05
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> arr1;
        int index = 0;
        for(int i = 0; i<nums.size(); i++){
            if(nums[i]!=val){
                nums[index++] = nums[i];
            }
        }
        return index;
    }
};