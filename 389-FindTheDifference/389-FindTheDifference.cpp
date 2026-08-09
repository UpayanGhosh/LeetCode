// Last updated: 10/08/2026, 02:35:01
class Solution {
public:
    char findTheDifference(string s, string t) {
        int n = s.length();
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        for(int i=0; i<n; i++) 
        if(s[i]!=t[i]) 
        return t[i];
        return t[n];
    }
};