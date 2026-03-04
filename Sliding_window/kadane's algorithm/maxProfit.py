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