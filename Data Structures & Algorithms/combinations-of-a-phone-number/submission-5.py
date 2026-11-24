class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        char_map = {"2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        def func(index,subset):
            if index == len(digits):
                result.append("".join(subset))
                return

            for i in char_map[digits[index]]:
                subset.append(i)
                func(index+1,subset)
                subset.pop()

        func(0,[])
        return result                        