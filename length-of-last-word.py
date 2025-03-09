# 58. Length of Last Word
# Difficulty level: Easy
# Top Interview 150
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring(a substring is a continuous non-empty sequence of characters within a string) consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
# Solution to the question
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
    #longest-common-prefix.py

# Here's how it works step by step:

# 1. s.strip() - This removes any leading and trailing whitespace from the string
# 2. .split(' ') - This splits the string into a list of words using space as the delimiter
# 3.  [-1] - This gets the last element of the list (the last word)
#4.  len() - This returns the length of that last word

# For example:

# For input "Hello World":

#-  After strip: "Hello World"
#-  After split: ["Hello", "World"]
#-  Last word: "World"
#-  Length: 5

# For input "   fly me   to   the moon  ":

#-  After strip: "fly me   to   the moon"
#-  After split: ["fly", "me", "to", "the", "moon"]
#- Last word: "moon"
#- Length: 4

# The solution handles all the constraints well:

# Works with multiple spaces between words
# Works with leading/trailing spaces
# Works with strings containing only letters and spaces
# Works with strings containing at least one word

# Time complexity is O(n) where n is the length of the string, as we need to traverse the string for both strip and split operations.
