class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 999999999
        maximum = 0

        # Go through all the prices
        for i in range(len(prices)):
            # Check if we have reached a minimum price
            if prices[i] < minimum:
                # set the new minimum price
                minimum = prices[i]
            # Check if the current profit - price > than the current max
            elif prices[i] - minimum > maximum:
                # Change the new maximum profit
                maximum = prices[i] - minimum

        return maximum

