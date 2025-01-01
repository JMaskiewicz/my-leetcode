"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/

"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                return True
            map[nums[i]] = 1
        return False

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
'''

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4]))