"""
169. Majority Element
https://leetcode.com/problems/majority-element/description/
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        for key in map:
            if map[key] > len(nums) // 2:
                return key
        return -1


solution = Solution()
print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([2,2,1,1,1,2,2]))