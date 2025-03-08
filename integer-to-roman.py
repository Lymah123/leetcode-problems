# 12. Integer to Roman
# Difficulty level: Medium
# Top Interview 150
# Seven different symbols represent Roman numerals with the following values:
# Symbol       Value
# I                 1
# V                5
# X                10
# L                50
# C                100
# D                500
# M               1000

# Roman numerals are formed by appending the conversions of decimal place values from the highest to lowest. COnverting a decimal place value into a Roman numeral has the folowing rules:

# . If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, substract its value, and convert the remainder to a Roman numeral.

#. If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1(I) less than 5(V): IV and 9 is (I) less than 10(X): IX. Only the following subractive forms are used: 4(IV), 9(IX), 40(XL), 90(XC), 400(CD), and 900(CM).

# . Only powers of 10(I, X,C,M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50(L), or 500(D) multiple times. If you need to append a symbol 4 times use the subtractive form.

# Given an integer, convert it to a Roman numeral.

# Example 1:
# Input: num = 3749
# Output: "MMMDCCXLIX"
# Explanation:
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
# 700 = DCC as 500 (D) + 100 (C) + 100 (C)
# 40 = XL as 10 (X) Less of 50 (L)
# 9 = IX as 1 (I) less of 10 (X)
# NOTE: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places.

# Example 2:
# Input: num = 58
# Output: "LVIII"

# Explanation:
# 50 = L
# 8 = VIII

# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation:
# 1000 = M
# 900 = CM as 1000 (M) less of 100 (C)
# 90 = XC as 100 (C) less of 10 (X)
# 4 = IV as 5 (V) less of 1 (I)

# Constraints:
# 1 <= num <= 3999

# Solution to the question  (using greedy algorithm)

class Solution:
    def intToRoman(self, num: int) -> str:
        # Define value-symbol pairs from largest to smallest
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        roman = ""
        for value, symbol in value_symbols:
            # Get the number of times this symbol should be repeated
            count = num // value
            # Add the symbol that many times
            roman += symbol * count
            # Subtract from the remaining number
            num %= value

        return roman

# Time complexity: O(1)
# Space complexity: O(1)

# What is Greedy algorithm?
# In computer science, a greedy algorithm is an algorithm that finds a solution to problems in the shortest time possible. It picks the path that seems optimal at the moment without regard for the overall optimization of the solution that would be formed.


