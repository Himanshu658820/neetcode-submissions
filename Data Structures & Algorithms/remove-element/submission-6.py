class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        res = []
        i = 0
        j = i + 1
        n = len(nums)
        while j<n:
            if nums[i] != val:
                i += 1
                

            elif nums[i] == val and nums[j] != val:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1

            j += 1

        count = 0
        for i in range(n-1,-1,-1):
            if nums[i] == val:
                count += 1
                nums.remove(val)

            else:
                break               

        return n - count
                       