from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        person_indexes = []
        for i, p in enumerate(seats):
            if p == 1:
                person_indexes.append(i)
        max_distance = 0
        for i in range(len(person_indexes)-1):
            max_distance = max(max_distance, (person_indexes[i+1] - person_indexes[i]) // 2)
        return max(max_distance, person_indexes[0], len(seats) - person_indexes[-1] - 1)


