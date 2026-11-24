class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*len(nums)
        def robber(index):
            if index == 0:
                return nums[index]
            if index < 0:
                return 0
            if dp[index] != -1:
                return dp[index]
            p = nums[index] + robber(index - 2)
            np = 0 + robber(index - 1)
            dp[index] = max(p,np)
            return dp[index]
        return robber(n - 1)    