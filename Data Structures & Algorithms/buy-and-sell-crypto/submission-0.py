class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for left_index in range(len(prices)):
            for right_index in range(left_index + 1, len(prices)):
                current_sum = prices[right_index] - prices[left_index]

                if (current_sum > maximum):
                    maximum = current_sum
        return maximum