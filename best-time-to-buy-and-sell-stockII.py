# 122. Best time to buy and sell stock II
# Difficulty level: Medium
# Array / String
# Top 150 interview questions
# You are given an array prices for which the ith element is the price of a given stock on day i.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it on one day and sell it on the same day.

# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a profit, so we do not buy the stock at all.

# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit


# Explanation:
# Initialization: We initialize total_profit to 0.
# Loop Through Prices: We start from the second day (index 1) and iterate through the prices array.
# Check for Profit: For each day, if the price of the current day (prices[i]) is higher than the price of the previous day (prices[i - 1]), we add the difference to total_profit.
# Return Result: After the loop, we return the total_profit.
