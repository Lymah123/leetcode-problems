# 209. Minimum Size SubArray Sum
# Difficulty level: Medium
# Top Interview 150

# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose length is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
# Explanation: The subarray [4] has the minimal length under the problem constraint.

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# Explanation: The subarray [1,1,1,1,1,1,1,1] has a sum less than target.

# Constraints:
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# Follow up: If you have figured out the O(n) solution, try coding another solution of O(n log(n)) time complexity.
#
# Solution
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(n):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
  
