class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one,zero = 0,0
        for two in range(0,len(nums)):
            temp = nums[two]
            nums[two] = 2

            if temp < 2:
                nums[one] = 1
                one += 1

            if temp < 1:
                nums[zero] = 0
                zero += 1    
        