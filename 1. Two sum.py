"""
1. Two Sum
https://leetcode.com/problems/two-sum/description/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        return []


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))