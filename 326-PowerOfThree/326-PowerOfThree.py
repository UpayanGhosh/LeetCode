# Last updated: 10/08/2026, 02:35:18
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 3 == 0 and n > 0:
            return self.isPowerOfThree(n // 3)
        else:
            return False