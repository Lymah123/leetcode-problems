# 167. Two Sum II - Input Array Is Sorted
# Difficulty level: Medium
# Topi Interview 150
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2, 3, 4], target = 6
# Output: [1, 3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 2, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1, 0], target = -1
# Output: [1, 2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

# Solution

# Approach
# 1. Two Pointers:
# - Initialize two pointers, left and right, at the beginning and end of the array, respectively.
# - While left is less than right:
#   - Calculate the sum of the elements at the left and right pointers.
#   - If the sum is equal to the target, return the indices of the two numbers (left + 1 and right + 1).
#   - If the sum is less than the target, increment the left pointer to increase the sum.
#   - If the sum is greater than the target, decrement the right pointer to decrease the sum.
# 2. Time Complexity:
# - O(n), where n is the length of the input array. We traverse the array once.
# 3. Space Complexity:
# - O(1), since we are using only a constant amount of extra space.

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Return 1-indexed positions as required
                return [left + 1, right + 1]
            elif current_sum < target:
                # If sum is too small, move left pointer to increase the sum
                left += 1
            else:
                # If sum is too large, move right pointer to decrease the sum
                right -= 1

        # The problem guarantees exactly one solution, we'll never reach here
        return []
