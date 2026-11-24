class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1,-1] for _ in range(len(prices))]
        def func(index,buy):
            if index == len(prices):
                return 0

            if dp[index][buy] != -1:
                return dp[index][buy]    

            if buy == 1:
                buy_profit = -prices[index] + func(index+1,0)
                not_buy = func(index + 1, 1)
                profit = max(buy_profit, not_buy)

            else:
                sell = prices[index] + func(index+1,1)
                not_sell = func(index+1,0)
                profit = max(sell,not_sell)

            dp[index][buy] = profit
            return dp[index][buy]

        return func(0,1)                
        