from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        in_degrees = [0]*n
        next_courses = [[] for _ in range(n)]
        for pre_c, next_c in relations:
            in_degrees[next_c-1] += 1
            next_courses[pre_c-1].append(next_c-1)
        queue = []
        costs = [0] * n
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                queue.append(i)
        while queue:
            course = queue.pop()
            costs[course] += time[course]
            for next_course in next_courses[course]:
                in_degrees[next_course] -= 1
                costs[next_course] = max(costs[next_course], costs[course])
                if in_degrees[next_course] == 0:
                    queue.append(next_course)
        return max(costs)

print(Solution().minimumTime(2,[[2,1]],[10000,10000]))