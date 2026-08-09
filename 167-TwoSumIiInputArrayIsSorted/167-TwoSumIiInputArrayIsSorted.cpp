// Last updated: 10/08/2026, 02:35:57
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        int n = nums.size();
        unordered_map<int,int> m;
        for(int i = 0; i<n; i++){
            int rem = target - nums[i];
            if(m.find(rem)!=m.end()){
                ans.push_back(m[rem]);
                ans.push_back(i+1);
            }
            else m[nums[i]]=i+1;
        }
        return ans;
    }
};