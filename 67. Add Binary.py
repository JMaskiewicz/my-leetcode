"""
67. Add Binary
https://leetcode.com/problems/add-binary/description/
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)

        for i in range(max_length - 1, -1, -1):
            sum_val = int(a[i]) + int(b[i]) + carry
            result = str(sum_val % 2) + result
            carry = sum_val // 2

        if carry:
            result = "1" + result

        return result

solution = Solution()
print(solution.addBinary("10001", "1101"))
print(solution.addBinary("1010", "1011"))