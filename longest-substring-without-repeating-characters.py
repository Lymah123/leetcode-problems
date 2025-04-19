# 3. Longest Substring Without Repeating Characters
# Difficulty level: Medium
# Top Interview 150

# Given a string s, find the longest substring without duplicate chararcters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Noice that the answer must e a substring, "pwke" is a subsequence and not a substring.

# Constraintss:
# <+ s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Solution
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_set = set()
        left = 0
        max_length = 0

        for right in range(n):
            # If we find a repeating character, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

                # Add the current character to the set
            char_set.add(s[right])

                # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length

    # This solution uses a slding window approach with a set to keep track of the characters in the current substring.

