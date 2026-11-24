class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 == 1:
            return False
        total = s // 2
        dp = [[-1 for _ in range(total+1)]for _ in range(n)]
        def func(index, total):
            if total == 0:
                return True
            if index == 0:
                return nums[index] == total
            if dp[index][total] != -1:
                return dp[index][total]    
            if nums[index] > total:
                pick = False
            else:
                pick = func(index - 1, total - nums[index])

            notpick = func(index - 1, total) 
            dp[index][total] = pick or notpick
            return dp[index][total]

        return func(n-1, total)       
        