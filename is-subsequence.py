# 392. Is Subsequence
# Difficulty level: Easy
# Top Interview 150
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers for both strings
        i, j = 0, 0

        # Traverse through both strings
        while i < len(s) and j < len(t):
            # If characters match, move pointer for s
            if s[i] == t[j]:
                i += 1
            # Always move pointer for t
            j += 1

        # If we've matched all characters of s, return True
        return i == len(s)

# Explanation:
# Pointers initialization: We start both pointers i and j at 0.

# While loop: The loop runs as long as there are characters in both s and t. If we find a match, we move the pointer i forward to look for the next character in s. In either case, j always moves forward since we're scanning through t.

# Return condition: After the loop ends, we check if i has reached the length of s. If it has, it means we've matched all characters of s in t in the correct order, so we return True.

# Time Complexity:
# O(n), where n is the length of string t. We traverse t once, and each character is compared at most once.

# Space Complexity:
# O(1) since we are using only a constant amount of extra space.

# Example:
# For the input s = "abc" and t = "ahbgdc", the function will return True because the characters of s appear in t in the correct order.

# For the input s = "axc" and t = "ahbgdc", the function will return False because the order of characters in s is not preserved in t.
