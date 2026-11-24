class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []
        def func(index,total,subset):
            if total == 0:
                result.append(subset.copy())
                return

            if total < 0:
                return

            for i in range(index,n):
                if i > index and candidates[i] == candidates[i-1]:
                    continue

                subset.append(candidates[i])
                sum = total - candidates[i]
                func(i+1,sum,subset)
                subset.pop()

        func(0,target,[])
        return result                    
        