// Last updated: 10/08/2026, 02:35:54
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0, ele, n = nums.size();
        for(int i = 0; i < n; i++){
            if(count == 0){
                count = 1;
                ele = nums[i];
            }else if(ele == nums[i]){
                count++;
            }else{
                count--;
            }
        }
        int ct = 0;
        for(int i = 0; i < n; i++){
            if(ele == nums[i]){
                ct++;
            }
        }
        if(ct > n/2) return ele;
        return -1;
    }
};