class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        m = max(d,key = d.get)
        return m       

        