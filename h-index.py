# 274
# Difficulty level: Medium
# Top 150 Interview
# Given an array of integers citations where citations[i] is the number of citation a researcher recieved for their ith paper, return compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them has received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1

# Constraints:
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000

# Approach:
# We sort the array in descending order. We iterate through the array and check if the current element is greater than or equal to the index. If it is, we return the index. If we reach the end of the array, we return the length of the array.

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)

        for i in range(n):
            if citations[i] < i + 1:
                return i

        return n



