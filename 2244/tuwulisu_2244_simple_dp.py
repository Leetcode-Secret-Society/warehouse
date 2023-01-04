class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        difficuly_counts = defaultdict(int)
        for task in tasks:
            difficuly_counts[task]+=1
        #print(difficuly_counts)
        count_round_map = {1: -1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2}
        def cal_round(count):
            if count in count_round_map:
                return count_round_map[count]
            else:
                round = cal_round(count-3) + 1
                count_round_map[count] = round
                return round
        ans = 0
        for count in difficuly_counts.values():
            round = cal_round(count)
            if round==-1:
                return -1
            ans += round
        return ans
