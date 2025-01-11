# Remove Element: Question 27- Top Interview 150 (Easy)
# Given an integer arrays NUMS and an integer VAL, remove all occurrences of VAL in NUMS in-place. The order of the elements may be changed. Then return the number of elements in NUMS which are not equal to VAL.

# Consider the number of elements in NUMS which are not equal to VAL be K, to get accepted, you need to do the following things:
# - Change the array NUMS such that the first K elements of NUMS contain the elements which are not equal to VAL. The remaining elements of NUMS are not important as well as the size of NUMS.
# - Return K.

# Custom judge: The judge will test your solution with the following code:

# int [] nums = [...]; // Input array
# int val = ...; // Value to remove
# int [] expectedNums = [...];  // The expected answer with correct lenght.
# val . // It is sorted with no values equaling

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actuallength; i++) {
#   assert nums[i] == expectedNums [i];
# }

# Example1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores).UnicodeTranslateError

# Example2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,2,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0,0,1,3, and 4. Note that the five elements can be returned in any order. It does not matter what you leave beyond the returned k(hence they are underscores).

# Constrainst:
# 0 <= nums.length <= 100
# 0 <= nums [i] <= 50
# 0 <= val <= 100

# Solution to the question
def removeElement(nums, val):
  # def removeElement(self, nums: List[int], val: int) -> int:
    # Initialize a pointer for the position to place non-val elements.
    k = 0
    # Iterate over the array
    for num in nums :
    # If the current number is not equal to val
      if num != val :
        # Place it in the position indicated by k
        nums[k] = num
        k += 1
    return k
