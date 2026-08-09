# Last updated: 10/08/2026, 02:36:14
class Solution(object):
    def maxProfit(self, prices):
        least_price = float('inf')  # Use 'inf' for positive infinity
        total_profit = 0

        for i in range(len(prices)):
            if prices[i] < least_price:
                least_price = prices[i]
            else:
                # Calculate the profit if selling today
                profit_if_sell_today = prices[i] - least_price

                # If the profit is positive, accumulate it in total_profit
                if profit_if_sell_today > 0:
                    total_profit += profit_if_sell_today

                    # Update least_price for the next potential buying opportunity
                    least_price = prices[i]

        return total_profit
        