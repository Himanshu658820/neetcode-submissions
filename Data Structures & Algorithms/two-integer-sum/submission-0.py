class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(0,n):
            remain = target - nums[i]
            if remain in dic:
                return [dic[remain], i]
            dic[nums[i]] = i
        return [i, dic[remain]]    