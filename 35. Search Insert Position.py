"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/description/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)

# binary search !
# this one is wrong

solution = Solution()
print(solution.searchInsert(nums = [1,3,5,6], target = 7))
print(solution.searchInsert(nums = [1,3,5,6], target = 5))
print(solution.searchInsert(nums = [1,3,5,6], target = 2))
print(solution.searchInsert(nums = [1], target = 2))