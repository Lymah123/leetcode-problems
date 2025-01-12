# Question: REMOVE MOVE DUPLICATES FROM SORTED ARRAY
# Given an integer array NUMS sorted in non-decreasing order, remove the duplicates in-place such that each unique element appearss only once. The relative order of the elements should be kept the same. Then return the number of bique elements in NUMS.

# - Consider the number of uniqe elements of NUMS to be K, to get accepted, you need to do the following things:
# Change the array NUMS such that the first K elements of NUMS contain the unique elements in the order they were present in NUMS initially. The remaining elements of NUMS are not important as well as the size of NUMS.
# - Return K.
# Custom Judge:
# int [] nums = [...]; // Input array
# int [] expectedNums = [...]; // The expected answer with correct length
# int k = removeDuplicates(nums); // Calls your implementation
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums =
# [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constarints:
# - 1 <= nums.length <= 3 * 104
# - -100 <= nums[i] <= 100
# - nums is sorted in non-decreasing order.

# # Solution

def removeDuplicates(nums):

  if not nums:
    return 0 # If the array is empty, return 0
  k = 1

# Traverse the array starting from the second element
  for i in range(1, len(nums)):
    # If the current element is not equal to the previous one, it is unique
    if nums[i] != nums[i - 1]:
      nums[k] = nums[i]
      k += 1

# Return the count of unique elements
  return k
