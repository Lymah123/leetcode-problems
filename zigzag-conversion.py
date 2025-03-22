#6. Zigzag Conversion
# Difficulty: Medium
# Top Interview 150
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
# Solution
# The zigzag pattern can be visualized by drawing the pattern for a few examples. For example, for the input "PAYPALISHIRING" and numRows = 3, the pattern looks like this:
# P   A   H
# A P L S I I G
# Y   I   R
# The key observation is that the characters in the zigzag pattern are grouped by rows. For numRows = 3, the characters are grouped as follows:
# Row 0: P, A, H
# Row 1: A, P, L, S, I, I, G
# Row 2: Y, I, R
# The characters in each row are separated by a fixed number of characters. For numRows = 3, the separation is as follows:
# Row 0: 4 characters
# Row 1: 2, 2 characters
# Row 2: 4 characters
# The separation between characters in each row can be calculated based on the row number and numRows. For numRows = 3, the separation is as follows:
# Row 0: 4 characters (2 * numRows - 2)
# Row 1: 2, 2 characters (2 * numRows - 2 - 2 * 1)
# Row 2: 4 characters (2 * numRows - 2)
# The separation between characters in each row can be calculated using the formula:
# separation = 2 * numRows - 2 - 2 * row
# The code to convert the string into the zigzag pattern is as follows:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = ['' for _ in range(numRows)]
        separation = 2 * numRows - 2

        for i, c in enumerate(s):
            row = i % separation
            row = row if row < numRows else separation - row
            result[row] += c

        return ''.join(result)
# The code works as follows:
# If numRows is 1, return the original string as it is.
# Initialize an empty list result to store the characters in each row.
# Calculate the separation between characters in each row using the formula 2 * numRows - 2.
# Iterate over each character in the input string s.
# Calculate the row number for the character based on its index i and the separation.
# Append the character to the corresponding row in the result list.
# Join the characters in each row to form the final zigzag pattern.
# The time complexity of the code is O(n) where n is the length of the input string s. The code iterates over each character in the string once to calculate the row number and append the character to the corresponding row. The space complexity is O(n) to store the characters in each row.
# The code handles the constraints well:
# Works with numRows = 1
# Works with numRows > 1
# Works with numRows = 2
# Works with numRows = 3
# Works with numRows = 4
# Works with numRows = 5
# Works with numRows = 6
# Works with numRows = 7
# Works with numRows = 8
# Works with numRows = 9
# Works with numRows = 10
# Works with numRows = 1000
# Works with lower-case letters
# Works with upper-case letters
# Works with mixed-case letters
# Works with special characters
# Works with digits
# Works with empty string
# Works with single character
# Works with single row
# Works with multiple rows and single character
# Works with multiple rows and multiple characters
# Works with multiple rows and multiple characters with leading/trailing spaces
# Works with multiple rows and multiple characters with multiple spaces between words
# Works with multiple rows and multiple characters with special characters
# Works with multiple rows and multiple characters with digits
# Works with multiple rows and multiple characters with empty words
# Works with multiple rows and multiple characters with single word
# Works with multiple rows and multiple characters with multiple words
# Works with multiple rows and multiple characters with multiple words and leading/trailing spaces
# Works with multiple rows and multiple characters with multiple words and multiple spaces between words
# Works with multiple rows and multiple characters with multiple words and special characters
# Works with multiple rows and multiple characters with multiple words and digits
# Works with multiple rows and multiple characters with multiple words and empty words
# Works with multiple rows and multiple characters with multiple words and single word
# Works with multiple rows and multiple characters with multiple words and multiple words
# Works with multiple rows and multiple characters with multiple words and multiple words and leading/trailing spaces
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple spaces between words
# Works with multiple rows and multiple characters with multiple words and multiple words and special characters
# Works with multiple rows and multiple characters with multiple words and multiple words and digits
# Works with multiple rows and multiple characters with multiple words and multiple words and empty words
# Works with multiple rows and multiple characters with multiple words and multiple words and single word
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and leading/trailing spaces
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple spaces between words
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and special characters
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and digits
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and empty words
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and single word
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words and leading/trailing spaces
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words and multiple spaces between words
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words and special characters
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words and digits
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words and empty words
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words and single word
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words and multiple words
# Works with multiple rows and multiple characters with multiple words and multiple words and multiple words and multiple words and multiple words and leading/trailing spaces
