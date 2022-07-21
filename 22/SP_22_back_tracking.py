class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1. ()
        # 2. ()() / (())
        # 3. ()()()/ (())() ()(())/ ((()))
        ans = []
        limit = 2 * n
        def backtrack(S = [], left = 0, right = 0):
            #((( -> (((,)))
            #(( -> ((,).()) -> ((,).)()
            #( -> (,).(()) -> (,).().()
            if left+right == limit:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
