"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i

        return -1
"""
        try:
            return haystack.index(needle)
        except: return -1
"""

solution = Solution()
print(solution.strStr(haystack = "a", needle = "a"))
print(solution.strStr(haystack="leetcode", needle="leeto"))
print(solution.strStr(haystack = "aysadbutsad", needle = "sad"))
