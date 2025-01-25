# Rotate Array: Given an array, rotate the array to the right by k steps, where k is non-negative.
# Difficulty: Medium
# Top Interview 150 Questions: #189

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
# ------------------------------------------------------------------------------------------------------------------------------------

# Approach:
# Solution:
# 1. We can use a temp array to store the elements of the original array.
# 2. Then we can copy the elements from the temp array to the original array after shifting the elements by k steps.
# 3. We can also use the slicing technique to achieve the same result.
# 4. We can also reverse the array and then reverse the first k elements and the last
#    n-k elements
# 5. We can also use the cyclic replacement technique to achieve the same result.
# ------------------------------------------------------------------------------------------------------------------------------------
# Time complexity: O(n)
# Space complexity: O(n)
# ------------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n # Effective rotation
    # Reverse the entire array
    nums.reverse()
    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    # Reverse the remaining elements
    nums[k:] = reversed(nums[k:])
