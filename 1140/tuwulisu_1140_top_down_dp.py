class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        prefix_sums = [0]
        for n in piles:
            prefix_sums.append(prefix_sums[-1]+n)
        #print(prefix_sums)
        optimal_dict = dict()
        def get_optimal(i, m):
            #print(f"get optimal: i={i}, m={m}")
            if (i, m) in optimal_dict:
                return optimal_dict[(i, m)]
            if i>=len(piles):
                optimal_dict[(i, m)] = 0
                return 0
            if len(piles) - i <= 2*m:
                got_stone = prefix_sums[-1] - prefix_sums[i]
                optimal_dict[(i, m)] = got_stone
                return got_stone
            max_take = 0
            for x in range(1, 2*m+1):
                opponent = get_optimal(i+x, max(x, m))
                remaining = prefix_sums[-1] - prefix_sums[i+x] - opponent
                me = prefix_sums[i+x] - prefix_sums[i] + remaining
                #print((i, m, x, ":"), me, opponent)
                max_take = max(max_take, me)

            optimal_dict[(i, m)] = max_take
            #print(f"final get optimal: i={i}, m={m}, make_take={max_take}")
            return max_take
        ans = get_optimal(0, 1)
        #print(optimal_dict)
        return ans
