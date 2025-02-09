"""
18. 4Sum
https://leetcode.com/problems/4sum/
"""

from typing import List

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.threeSum(nums, i, target, result)
        return result

    def threeSum(self, nums: List[int], index: int, target: int, result: List[List[int]]):
        for j in range(index + 1, len(nums)):
            if j > index + 1 and nums[j] == nums[j - 1]:
                continue
            self.twoSum(nums, index, j, target, result)

    def twoSum(self, nums: List[int], first: int, second: int, target: int, result: List[List[int]]):
        left, right = second + 1, len(nums) - 1
        while left < right:
            total = nums[first] + nums[second] + nums[left] + nums[right]
            if total == target:
                result.append([nums[first], nums[second], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1