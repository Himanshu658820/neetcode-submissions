class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        res = []
        for i in range(0,n):
            if nums[i] not in dic:
                dic[nums[i]] = 1

            else:
                dic[nums[i]] += 1
        for key,value in dic.items():
            if value > n//3:
                res.append(key)
        return res                    

        