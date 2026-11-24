class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""]*(2*n)
        result = []
        self.func(0,0,brackets,result)
        return result

    def func(self,index,total,brackets,result):
        if index == len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return 

        if total < 0:
            return

        if total > len(brackets):
            return 

        brackets[index] = "("
        sum = total + 1
        self.func(index+1,sum,brackets,result)

        brackets[index] = ")"
        sum = total - 1
        self.func(index+1,sum,brackets,result)    
        