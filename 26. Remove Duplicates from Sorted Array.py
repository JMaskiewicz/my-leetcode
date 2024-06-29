"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        insert_pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        return insert_pos

solution = Solution()
print(solution.removeDuplicates(nums = [1,1,2]))