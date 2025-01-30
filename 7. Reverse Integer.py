"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10

        reversed_x *= sign
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0

        return reversed_x