# 42. Tapping Rain Water
# Difficulty level: Hard
# Top Interview 150
# Given n non-negative integers representing an elevation map where the width of each bar is 1,compute how much water it can trap after raining

# Example 1:
# An image

# Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input height = [4, 2, 0, 3, 2, 5]
# Output: 9

# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= length <= 105

# Solution to the question
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max = right_max = water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water
