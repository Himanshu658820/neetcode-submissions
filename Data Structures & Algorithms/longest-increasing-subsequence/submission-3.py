class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        def func(index,prev):
            count = 0
            if index < 0:
                return 0
            if dp[index][prev] != -1:
                return dp[index][prev]    
            pick = 0    
            if prev == -1 or nums[index] < nums[prev]:
                pick = 1 + func(index - 1,index)

            not_pick = func(index-1, prev)
            dp[index][prev] = max(pick,not_pick)
            return dp[index][prev]
        return func(n-1, -1)    



        