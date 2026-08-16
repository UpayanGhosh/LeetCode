# Last updated: 16/08/2026, 09:04:03
1class Solution(object):
2    def nearestDrone(self, drones, target):
3        tx = target[0]
4        ty = target[1]
5        min_distance = 9999999999
6        index = -1
7        for i, (x,y,r) in enumerate(drones):
8            distance = abs(x - tx) + abs(y - ty)
9            if distance <= r and distance < min_distance:
10                min_distance = distance
11                index = i
12        return index
13        