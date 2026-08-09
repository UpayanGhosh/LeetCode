// Last updated: 10/08/2026, 02:34:24
class Solution {
public:
    int fib(int n) {
        if(n <=1) return n;
        return fib(n - 1) + fib(n - 2);
    }
};