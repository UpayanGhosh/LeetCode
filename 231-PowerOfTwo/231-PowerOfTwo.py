# Last updated: 10/08/2026, 02:35:40
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 == 0 and n > 0:
            return self.isPowerOfTwo(n // 2)
        else:
            return False
        