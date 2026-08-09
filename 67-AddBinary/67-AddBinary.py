# Last updated: 10/08/2026, 02:36:29
class Solution(object):
    def addBinary(self, a, b):
        num1 = int(a,2)
        num2 = int(b,2)
        sum = num1 + num2
        return bin(sum)[2:]
        