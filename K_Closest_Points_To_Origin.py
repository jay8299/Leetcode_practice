#https://leetcode.com/problems/k-closest-points-to-origin/
"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


84 / 84 test cases passed.
Status: Accepted
Runtime: 676 ms
Memory Usage: 19.7 MB
"""
from math import sqrt
from collections import defaultdict


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kmap=defaultdict(list)
        for point in points:
            x=sqrt(point[0]**2+point[1]**2)
            kmap[x].append(point)
        flag=0
        kpoints=[]
        for i in sorted(kmap.keys()):
            for j in kmap[i]:
                k-=1
                kpoints.append(j)
                if k==0:
                    flag=1
                    break
            if(flag):
                break
        return kpoints