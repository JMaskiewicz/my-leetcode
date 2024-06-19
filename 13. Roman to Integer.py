"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/description/
"""



class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        combinations = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
        i = 0
        number = 0
        while i < len(s):
            if s[i:i+2] in combinations and i+1 < len(s):
                number += roman_to_int[s[i + 1]] - roman_to_int[s[i]]
                i += 2
            else:
                number += roman_to_int[s[i]]
                i += 1

        return number

solution = Solution()
print(solution.romanToInt("LVIII"))