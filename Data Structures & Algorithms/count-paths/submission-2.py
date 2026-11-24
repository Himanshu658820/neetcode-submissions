class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp  = [[-1]*n for _ in range(m)]
        def func(r,c):
            if r == 0 and c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            left = func(r,c-1)
            up = func(r - 1, c)            
            dp[r][c] = left + up

            return dp[r][c]
        return func(m-1,n-1)    
              
        