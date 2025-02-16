# Top 150 interview question
# 238. Product of Array Except Self
# Difficulty: Medium
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# THe product of any prefix or suffix of nums is not guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answers[i] fits in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Approach:

# 1. Initialize two arrays, left and right where left[i] represents the product of all the elements to the left of nums[i] and right[i] represents the product of all the elements to the right of nums[i].

# 2. We can build these arrays by iterating through nums in two passes. In the first pass, we fill the left array by setting left[i] = left[i - 1] * nums[i - 1]. In the second pass, we fill the right array by setting right[i] = right[i + 1] * nums[i + 1].

# 3. Finally, we build the answer array by iterating through nums. For each element in nums, we set answer[i] = left[i] * right[i].

# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    left = [0] * n
    right = [0] * n
    answer = [0] * n

    left[0] = 1
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    right[n - 1] = 1
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        answer[i] = left[i] * right[i]

    return answer


