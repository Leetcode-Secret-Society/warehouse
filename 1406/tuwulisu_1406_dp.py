class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        prefix_sums = [0]
        for n in stoneValue:
            prefix_sums.append(prefix_sums[-1]+n)
        max_score_memo = dict()
        def get_max_score(offset):
            if offset in max_score_memo:
                return max_score_memo[offset]
            if offset >= len(stoneValue):
                return 0
            max_taken = float('-inf')
            for taken_stone in range(1,4):
                opponent_taken = get_max_score(offset+taken_stone)
                #print(offset, taken_stone)
                if offset+taken_stone>=len(stoneValue):
                    me_taken = prefix_sums[-1] - prefix_sums[offset]
                else:
                    remaining = prefix_sums[-1] - prefix_sums[offset+taken_stone] - opponent_taken
                    me_taken = prefix_sums[offset+taken_stone] - prefix_sums[offset] + remaining
                max_taken = max(max_taken, me_taken)
            max_score_memo[offset] = max_taken
            return max_taken
        Alice_max = get_max_score(0)
        Bob_max = prefix_sums[-1] - Alice_max
        #print(Alice_max, Bob_max)
        if Alice_max > Bob_max:
            return "Alice"
        elif Alice_max < Bob_max:
            return "Bob"
        else:
            return "Tie"
