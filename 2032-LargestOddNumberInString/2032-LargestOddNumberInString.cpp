// Last updated: 10/08/2026, 02:33:43
class Solution {
public:
    string largestOddNumber(string num) {
        // scan from right to left for the first odd digit
        for (int i = num.size() - 1; i >= 0; --i) {
            int d = num[i] - '0';
            if (d % 2 == 1) {
                // once we find it, everything to its right is chopped off,
                // so the largest odd-numbered suffix is num[0..i]
                return num.substr(0, i + 1);
            }
        }
        // if no odd digit, there is no odd-numbered suffix
        return "";
    }
};
