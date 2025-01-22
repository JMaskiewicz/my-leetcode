"""
29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1

        return result if sign else -result