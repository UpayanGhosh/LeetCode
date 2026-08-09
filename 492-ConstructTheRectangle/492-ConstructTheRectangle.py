# Last updated: 10/08/2026, 02:34:48
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L = int(math.sqrt(area))
        while True:
            W = area / L
            if W.is_integer():
                if L > W:
                    return [L , int(W)]
                else:
                    return [int(W) , L]
            L -=1