"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/submissions/1507575532/

"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_pos] = nums[i]
                zero_pos += 1
        for i in range(zero_pos, len(nums)):
            nums[i] = 0
        return nums


solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
