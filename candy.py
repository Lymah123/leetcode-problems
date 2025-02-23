# 135. Candy
# Difficulty level: Hard
# Top 150 Interview
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:

# - Each child must have at least one candy.
# - Children with a higher rating get more candies than their neighbors.

# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.

# Constraints:
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104
# Approach:
# We can solve this problem using two passes. In the first pass, we initialize the candies array with 1. We iterate from left to right and update the candies array based on the ratings array. If the current rating is greater than the previous rating, we increment the candies array. In the second pass, we iterate from right to left and update the candies array based on the ratings array. If the current rating is greater than the previous rating, we increment the candies array. Finally, we return the sum of the candies array.

from typing import List

def candy(ratings: List[int]) -> int:
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

# Time Complexity: O(n)
# Space Complexity: O(n)

