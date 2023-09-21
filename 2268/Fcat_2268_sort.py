from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count_map = Counter(s)
        count_list = [(count,c) for c, count in count_map.items()]
        count_list.sort(reverse=True)

        result = 0
        presses = 0
        for i in range(len(count_list)):
            if i % 9 == 0:
                presses += 1
            result += count_list[i][0] * presses

        return result
