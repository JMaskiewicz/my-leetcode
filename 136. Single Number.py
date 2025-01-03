"""
136. Single Number
https://leetcode.com/problems/single-number/description/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                del freq[num]
            else:
                freq[num] = 1

        return list(freq.keys())[0]


solution = Solution()
print(solution.singleNumber([4,1,2,1,2]))
print(solution.singleNumber([2,2,1]))
print(solution.singleNumber([2]))