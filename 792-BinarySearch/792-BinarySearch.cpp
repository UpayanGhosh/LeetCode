// Last updated: 10/08/2026, 02:34:33
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int high = nums.size()-1;
        int low = 0;
        while(low<=high){
            int mid = low + (high-low)/2;
            if(target == nums[mid]) return mid;
            else if(nums[mid]<target) low = mid+1;
            else high--;
        }
        return -1;
    }
};