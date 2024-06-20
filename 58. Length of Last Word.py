"""
58. Length of Last Word

https://leetcode.com/problems/length-of-last-word/description/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = list(filter(None, s.split(' ')))[-1]
        return len(x)

solution = Solution()
print(solution.lengthOfLastWord(s = "luffy is still joyboy"))
print(solution.lengthOfLastWord(s = "   fly me   to   the moon  "))
print(solution.lengthOfLastWord(s = "Hello World"))
