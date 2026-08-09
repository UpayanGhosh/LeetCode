# Last updated: 10/08/2026, 02:33:51
class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        count = 0
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            ans += word1[i] + word2[i]
        ans += word1[min_len:] + word2[min_len:]
        return ans 
        