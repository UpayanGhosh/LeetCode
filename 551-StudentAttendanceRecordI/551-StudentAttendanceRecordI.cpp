// Last updated: 10/08/2026, 02:34:52
class Solution {
public:
    bool checkRecord(string s) {
        int count = 0;
        int flag = 0;
        for(int i = 0; i<s.size(); i++){
            if(s[i] == 'A') count++;
            if(s[i] == 'L' && s[i+1] == 'L' && s[i+2] == 'L') flag = 1;
        }
        if(count<2 && flag != 1) return true;
        else return false;
    }
};