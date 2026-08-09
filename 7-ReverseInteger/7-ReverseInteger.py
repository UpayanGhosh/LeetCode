# Last updated: 10/08/2026, 02:37:25
class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648


        sign = -1 if x < 0 else 1
        

        reversed_number = int(str(abs(x))[::-1])
        

        reversed_number *= sign
        

        if reversed_number < INT_MIN or reversed_number > INT_MAX:
            return 0
        
        return reversed_number
