# Top Interview 150: #169
# Difficulty: Easy

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than [n / 2] times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3, 2, 3]
# Output: 3

# Example 2:
# Input: nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# Approach:
# 1. We will use Boyer-Moore Voting Algorithm to solve this problem.
# 2. We will keep track of the majority element and its count.
# 3. If the count becomes 0, we will update the majority element.
# 4. We will return the majority element as the answer.

from typing import list

def majorityElement(nums: list[int]) -> int:
  # Initialize variables for the candidate and count
  candidate = None
  count = 0

  # First pass to find the majority element candidate

  for num in nums:
    if count == 0:
      candidate = num

    count += 1 if num == candidate else -1

  return candidate

