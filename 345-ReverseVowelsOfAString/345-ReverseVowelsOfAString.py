# Last updated: 10/08/2026, 02:35:07
class Solution(object):
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        i, j = 0, len(s) - 1
        s = list(s)  # Convert the string to a list to make it mutable

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                # Swap the vowels using a temporary variable
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            elif s[i] in vowels:
                j -= 1
            elif s[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1

        return "".join(s)
        