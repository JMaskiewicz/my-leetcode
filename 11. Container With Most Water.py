"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            length = min(height[left], height[right])
            max_area = max(max_area, width * length)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area