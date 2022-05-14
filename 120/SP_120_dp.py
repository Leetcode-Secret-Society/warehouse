class Solution:
    def inf():
        return math.inf
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = Solution.inf()
        dp = defaultdict(Solution.inf)
        for t_height in range(len(triangle)):
            if t_height == 0:
                dp[(0,0)] = triangle[0][0]
            else :
                for i in range(t_height+1):
                    # print(f"{i=}-{t_height=}")
                    dp[(t_height, i)] = triangle[t_height][i] + min(dp[(t_height -1, i-1)], dp[(t_height -1, i)])
                    
            # print(dp)
        for i in range(len(triangle[t_height])):
            final_value = dp[(t_height, i)]
            result = min(result, final_value)
        return result
                    
