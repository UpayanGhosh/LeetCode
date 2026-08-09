# Last updated: 10/08/2026, 02:33:54
class Solution(object):
    def largestAltitude(self, gain):
        altitudes = [0] * (len(gain)+1)
        for i in range(len(gain)):
            altitudes[i+1] = altitudes[i] + gain[i]
        return max(altitudes)
        