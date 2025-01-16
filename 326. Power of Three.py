"""
326. Power of Three
https://leetcode.com/problems/power-of-three/
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Maximum power of 3 within the 32-bit integer range
        max_power_of_three = 1162261467  # 3^19
        return n > 0 and max_power_of_three % n == 0