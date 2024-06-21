"""
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/description/

"""
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        while num >= 1000:
            num = num - 1000
            roman = roman + 'M'
        if num >= 900:
            num = num - 900
            roman = roman + 'CM'
        while num >= 500:
            num = num - 500
            roman = roman + 'D'
        if num >= 400:
            num = num - 400
            roman = roman + 'CD'
        while num >= 100:
            num = num - 100
            roman = roman + 'C'
        if num >= 90:
            num = num - 90
            roman = roman + 'XC'
        while num >= 50:
            num = num - 50
            roman = roman + 'L'
        if num >= 40:
            num = num - 40
            roman = roman + 'XL'
        while num >= 10:
            num = num - 10
            roman = roman + 'X'
        if num >= 9:
            num = num - 9
            roman = roman + 'IX'
        while num >= 5:
            num = num - 5
            roman = roman + 'V'
        if num >= 4:
            num = num - 4
            roman = roman + 'IV'
        while num >= 1:
            num = num - 1
            roman = roman + 'I'
        return roman'''

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        roman_table = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'],
            [50, 'L'],
            [40, 'XL'],
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I'],
        ]
        for i in roman_table:
            while num >= i[0]:
                roman += i[1]
                num -= i[0]

        return roman

solution = Solution()
print(solution.intToRoman(num = 58))
print(solution.intToRoman(num = 1994))
print(solution.intToRoman(num = 3749))