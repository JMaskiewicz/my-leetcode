"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini, maxi = min(strs), max(strs)  # something like sorting
        # next we compare only these 2 as if those 2 have common rest also need to have

        for i in range(len(mini)):
            if mini[i] != maxi[i]:
                return mini[:i]
        return mini


solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))