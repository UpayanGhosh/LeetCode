// Last updated: 10/08/2026, 02:34:55
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int maxCount = 0;
        for (int num : nums) {
            if (num == 1) {
                count++;
            } else {
                maxCount = max(maxCount, count);
                count = 0;
            }
        }
        // Check last segment if array ends with 1
        maxCount = max(maxCount, count);
        return maxCount;
    }
};
