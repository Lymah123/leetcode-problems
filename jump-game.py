# 55. JUMP GAME
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: num = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: num = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# Approach:
# We start from the last index and move backwards. If we can reach the last index from the current index, we update the last index to the current index. If we reach the first index, we return True, otherwise False.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i

        return last_index == 0

# Time Complexity: O(n)
# Space Complexity: O(1)


