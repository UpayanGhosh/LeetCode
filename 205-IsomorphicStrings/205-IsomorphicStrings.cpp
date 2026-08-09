// Last updated: 10/08/2026, 02:35:41
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int n = s.size();
        if(s.size() != t.size()) return false;
         unordered_map<char,char> mapST, mapTS;
        for(int i = 0; i < n; i++){
            if(mapST[s[i]] == 0 && mapTS[t[i]] == 0){
                mapST[s[i]] = t[i];
                mapTS[t[i]] = s[i];
            }else if(mapST[s[i]] != t[i] || mapTS[t[i]] != s[i]){
                return false;
            }
        }
        return true;
    }
};