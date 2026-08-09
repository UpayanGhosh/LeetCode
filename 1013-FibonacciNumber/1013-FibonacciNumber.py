# Last updated: 10/08/2026, 02:34:29
class Solution(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return n
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        i = 2
        while i <= n:
            dp[i] = dp[i - 1] + dp[i - 2]
            i += 1
        return dp[n]
