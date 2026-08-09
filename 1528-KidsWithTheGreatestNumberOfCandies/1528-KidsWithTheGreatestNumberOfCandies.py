# Last updated: 10/08/2026, 02:34:04
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        answer = []
        max_ele = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_ele:
                answer.append(True)
            else:
                answer.append(False)
        return answer

        