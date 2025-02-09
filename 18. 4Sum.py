"""
18. 4Sum
https://leetcode.com/problems/4sum/
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.three_sum(nums, i, target, result)
        return result