"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = ''
        longest = ''

        for i in s:
            if i in letters:
                if len(letters) > len(longest):
                    longest = letters
                letters = letters.split(i)[-1]
            letters = letters + i

        if len(letters) > len(longest):
            return len(letters)
        return len(longest)



solution = Solution()
print(solution.lengthOfLongestSubstring(s = "abcabcbb"))
print(solution.lengthOfLongestSubstring(s = "bbbbb"))
print(solution.lengthOfLongestSubstring(s = "pwwkew"))
print(solution.lengthOfLongestSubstring(s = "abcabcbb"))
print(solution.lengthOfLongestSubstring(s =" "))

print(solution.lengthOfLongestSubstring(s = "aab"))
print(solution.lengthOfLongestSubstring(s = "jbpnbwwd"))