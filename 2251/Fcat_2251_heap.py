from typing import List
from heapq import heappop, heappush


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        people_set = list(set(people))
        people_set.sort()
        i = j = cur_flowers = 0
        time_flower = {}
        flowers_wither_times = []
        while j < len(people_set):
            while i < len(flowers) and people_set[j] >= flowers[i][0]:
                cur_flowers += 1
                heappush(flowers_wither_times, flowers[i][1])
                i += 1
            while flowers_wither_times and flowers_wither_times[0] < people_set[j]:
                heappop(flowers_wither_times)
                cur_flowers -= 1
            time_flower[people_set[j]] = cur_flowers
            j += 1
        result = [0] * len(people)
        for i in range(len(people)):
            result[i] = time_flower[people[i]]
        return result

