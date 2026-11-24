class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1]*n    
        def robber(nums,index):
            if index == 0:
                return nums[index]

            if dp[index] != -1:
                return dp[index]

            if index > 1:         
                pick = nums[index] + robber(nums,index-2)

            else:
                pick = nums[index]

            np = robber(nums,index-1)

            dp[index] =  max(pick,np)
            return dp[index]
        
        r1 = robber(nums[:n-1] , n - 2)
        dp = [-1]*n
        r2 = robber(nums[1:] , n-2)
        return max(r1 , r2)