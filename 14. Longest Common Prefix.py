"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the lexicographically smallest and largest strings
        mini, maxi = min(strs), max(strs)

        # Iterate through the characters of the smallest string
        for i in range(len(mini)):
            # Compare characters at the same position in both strings
            if mini[i] != maxi[i]:
                # Return the substring from the start to the first differing character
                return mini[:i]

        # If no differing character is found, return the entire smallest string
        return mini


solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))