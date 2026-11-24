class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1,-1] for _ in range(len(prices) + 1)]
        n = len(prices)
        def func(index,buy):
            dp[len(prices)][0] = 0
            dp[len(prices)][1] = 0
            
            for index in range(n-1,-1,-1):
                for buy in range(0,2):
                    if buy == 1:
                        buy_profit = -prices[index] + dp[index+1][0]
                        not_buy = dp[index + 1][1]
                        profit = max(buy_profit, not_buy)

                    else:
                        sell = prices[index] + dp[index+1][1]
                        not_sell = dp[index+1][0]
                        profit = max(sell,not_sell)
                    dp[index][buy] = profit
            return dp[0][1]                
        return func(n,1)                
        