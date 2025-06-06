# 125. Valid Palindrome
# Dificulty level: Easy
# Top Interview 150
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = " A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = " Race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

# Constraints:
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1: Using string slicing
        # First, filter out non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        # Check if the string equals its reverse
        return s == s[::-1]

        # Solution 2: Using two pointers
        """
        # First, filter out non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        """

        # Solution 3: Using deque
        """
        from collections import deque
        # First, filter out non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        s = deque(s)

        while len(s) > 1:
            if s.popleft() != s.pop():
                return False
        return True
        """
