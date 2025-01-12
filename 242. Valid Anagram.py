"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in set(s): # ! set is faster than list
            if s.count(char) != t.count(char):
                return False
        return len(s) == len(t)


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))