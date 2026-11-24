class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n
        p,s = 1,1

        for i in range(n):
            prefix[i] = p
            p = p * nums[i]

        nums[:] = nums[::-1]    

        for i in range(n):
            suffix[i] = s
            s = s * nums[i]

        suffix[:] = suffix[::-1]    


        result = [a * b for a, b in zip(prefix, suffix)]
        return result



            
        