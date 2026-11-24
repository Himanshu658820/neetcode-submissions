class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*n
        def func(i,cost):
            if i == 0:
                return cost[i]
            if dp[i] != -1:
                return dp[i]    
            if i == 1:
                return cost[i]
            prev2 = cost[i] + func(i - 2, cost)
            prev = cost[i] + func(i - 1, cost)
            dp[i] = min(prev,prev2)
            return dp[i]

        return min(func(n-1,cost), func(n - 2, cost))            

        