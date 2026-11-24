class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        p,s = 1,1

        for i in range(n):
            prefix[i] = p
            p = p * nums[i]   

        for i in range(n - 1, -1, -1):
            suffix[i] = s
            s *= nums[i]  

        result = [a * b for a, b in zip(prefix, suffix)]
        return result



            
        