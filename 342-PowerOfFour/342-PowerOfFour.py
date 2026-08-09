# Last updated: 10/08/2026, 02:35:11
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 4 == 0 and n > 0:
            return self.isPowerOfFour(n // 4)
        else:
            return False
        