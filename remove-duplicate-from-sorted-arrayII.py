# Top Interview 150: #80
# Difficulty: Medium

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
# Since it is impossible to change the lenght of the array in some langueages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.

# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: It doesn't matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_]

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.


# Approach:
# 1. We will use two pointers to solve this problem.
# 2. We will keep track of the count of the current element.
# 3. If the count is less than 2, we will increment the pointer and copy the element to the pointer.
# 4. If the count is greater than 2, we will just increment the pointer.
# 5. We will return the pointer as the length of the array.

from typing import List

def removeDuplicates(nums):
  # If the array has less than 3 elements, all elements are allowed
  if len(nums) <= 2:
    return len(nums)

  # Pointer to replace the next valid element

  k = 2

  # Start iterating from the third element
  for i in range(2, len(nums)):
    # If the current element is different from the element at `k-2` position, we can replace the element at `k` position
    # It means we can allow this element

    if nums[i] != nums[k - 2]:
      nums[k] = nums[i]
      k += 1

# Return the count of valid elements
  return k
