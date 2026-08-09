// Last updated: 10/08/2026, 02:33:40
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        int positiveCount = 0;
        int negativeCount = 1;
        vector<int> arr(n);
        for(int i = 0; i < n; i++){
            if(nums[i] > 0){
                arr[positiveCount] = nums[i];
                positiveCount +=2;
            }else{
                arr[negativeCount] = nums[i];
                negativeCount +=2;
            }
        }
        return arr;
    }
};