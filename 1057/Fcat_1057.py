from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        bike_chose = [False] * len(bikes)
        pairs = []
        for i in range(len(workers)):
            worker_x, worker_y = workers[i]
            for j in range(len(bikes)):
                bike_x, bike_y = bikes[j]
                distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)
                pairs.append((distance, i, j))
        pairs.sort()
        result = [-1] * len(workers)
        for pair in pairs:
            _, worker_candidate, bike_candidate = pair
            if result[worker_candidate] == -1 and not bike_chose[bike_candidate]:
                result[worker_candidate] = bike_candidate
                bike_chose[bike_candidate] = True
        return result

print(Solution().assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))