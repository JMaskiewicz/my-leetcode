"""
66. Plus One
https://leetcode.com/problems/plus-one/description/
"""


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):  #range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


solution = Solution()
print(solution.plusOne(digits = [9]))
print(solution.plusOne(digits = [1,2,3]))
print(solution.plusOne(digits = [4,3,2,1]))