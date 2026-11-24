class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def func(index,subset):
            if index == n:
                res.append(subset.copy())
                return

            #pick
            subset.append(nums[index])
            func(index+1,subset)

            #backtrack
            subset.pop()

            #not_pick
            func(index+1,subset)

            return res
        return func(0,[])        

        