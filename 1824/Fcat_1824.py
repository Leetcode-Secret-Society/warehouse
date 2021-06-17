from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        min_jump = 0
        current_route = {2}

        for i, obstacle in enumerate(obstacles):
            if obstacle in current_route:
                current_route.remove(obstacle)
                if not current_route:
                    min_jump += 1
                    for lane in [1, 2, 3]:
                        if lane != obstacle and lane != obstacles[i-1]:
                            current_route.add(lane)

        return min_jump



