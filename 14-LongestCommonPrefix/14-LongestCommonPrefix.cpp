// Last updated: 10/08/2026, 02:37:18
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        int n = strs.size();
        string ans = "";
        string start = strs[0];
        string end = strs[n - 1];
        for(int i = 0; i < start.size(); i++){
            if(start[i] == end[i]){
                ans += start[i];
            }else{
                break;
            }
        }
        return ans;
    }
};