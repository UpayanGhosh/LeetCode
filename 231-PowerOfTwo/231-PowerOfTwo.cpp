// Last updated: 10/08/2026, 02:35:44
class Solution {
public:
    bool isPowerOfTwo(int n) {
        for(int i = 0; i<31; i++){
            if(n == pow(2,i))
                return true;
        }
        return false;
    }
};