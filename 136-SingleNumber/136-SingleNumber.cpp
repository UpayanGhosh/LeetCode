// Last updated: 10/08/2026, 02:36:05
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for(int i = 0; i < n-1; i++){
            if(nums[i] != nums[i+1]){
                return nums[i];
            }
            i+=1;
        }
        return nums[n-1];
    }
};