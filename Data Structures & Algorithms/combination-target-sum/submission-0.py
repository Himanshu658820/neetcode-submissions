class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def func(index,total,subset):
            if total == target:
                res.append(subset.copy())
                return

            if index == len(nums):
                return     

            if total > target:
                return 

            subset.append(nums[index])
            sum = total + nums[index]
            func(index,sum,subset)
            subset.pop()
            sum = total

            func(index + 1,sum,subset)            

        func(0,0,subset)
        return res  