# 151. Reverse Words in a String
# Difficulty level: Medium
# Top Interview 150
# Given an input string s, reverse the other of the words.
# A word is defined as a sequence of non-space characters. The word s will be separarated by at least one space and there will be no leading or trailing spaces or multiple spaces between words. The returned string should only have a single space separating the words. Do not include aby extra spaces.

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good  example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
# Solution to the question
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        words.reverse()

        return " ".join(words)
    
# Here's how it works step by step:
# 1. s.split() - This splits the string into a list of words using space as the delimiter
# 2. reversed() - This reverses the order of the words in the list
# 3. " ".join() - This joins the words in the list back into a string, using space as the delimiter
# For example:
# For input "the sky is blue":
# - After split: ["the", "sky", "is", "blue"]
# - After reversed: ["blue", "is", "sky", "the"]
# - After join: "blue is sky the"
# For input "  hello world  ":
# - After split: ["hello", "world"]
# - After reversed: ["world", "hello"]
# - After join: "world hello"
# For input "a good  example":
# - After split: ["a", "good", "example"]
# - After reversed: ["example", "good", "a"]
# - After join: "example good a"
# The solution handles all the constraints well:
# Works with leading/trailing spaces
# Works with multiple spaces between words
# Handles empty string
# Works with single word
# Works with spaces only
# Works with spaces and single word
# Works with spaces and multiple words
# Works with spaces and multiple words and leading/trailing spaces
# Time complexity is O(n) where n is the length of the string, as we need to traverse the string for both split and join operations.


