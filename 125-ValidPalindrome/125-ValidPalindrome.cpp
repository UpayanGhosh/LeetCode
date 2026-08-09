// Last updated: 10/08/2026, 02:36:10
class Solution {
public:
    bool func(int i, int n, vector<char> &arr) {
        if(i >= n / 2) return true;
        if(arr[i] != arr[n - i - 1]) return false;
        return func(i + 1, n, arr);
    }
    
    bool isPalindrome(string s) {
        vector<char> arr;
        for(char c : s){
            if(isalnum(c)){
                arr.push_back(tolower(c));
            }
        }
        return func(0, arr.size(), arr);
    }
};
