"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        combinations = {'()', '[]', '{}'}
        right = {')', '}', ']'}

        left_open = ''
        for char in s:
            left_open += char
            if char in right:
                if left_open[-2:] in combinations:
                    left_open = left_open[:-2]
                else:
                    return False
        if left_open == '':
            return True
        return False

solution = Solution()
print(solution.isValid("{[]}{}"))
print(solution.isValid("{[]}[{]}"))
print(solution.isValid("(("))
