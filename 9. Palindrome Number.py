"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/description/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if str(x) == str(x)[::-1]:
            return True

        return False