"""
15. 3Sum
https://leetcode.com/problems/3sum/
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.two_sum(nums, i, result)
        return result