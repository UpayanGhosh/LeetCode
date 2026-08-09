// Last updated: 10/08/2026, 02:34:17
class Solution {
public:
    int bitwiseComplement(int n) {
        int m = n;
        int mask = 0;
        if(n ==0)
            return 1;
        while(m!=0){
            mask = (mask << 1) | 1;
            m = m >> 1;
        }
        int ans = (~n) & mask;
        return ans;
    }
};

//For understanding the concept refer to https://youtu.be/0fwrMYPcGQ0

