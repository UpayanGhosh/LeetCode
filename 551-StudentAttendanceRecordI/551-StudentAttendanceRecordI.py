# Last updated: 10/08/2026, 02:34:47
class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        flag = False

        for i in range(len(s)):
            if s[i] == 'A':
                count += 1
            if i < len(s) - 2 and s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                flag = True

        return count < 2 and not flag
