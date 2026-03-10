""" Algorithm

Traverse the price array starting from index 1.

Compute the daily difference between current price and previous price.

Add the difference to current_sum.

If current_sum becomes negative, reset it to 0.

Track the maximum profit using max_sum.

Return max_sum after traversal. """

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        current_sum = 0
        max_sum = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            current_sum = max(0, current_sum + diff)  # reset if negative
            max_sum = max(max_sum, current_sum)

        return max_sum