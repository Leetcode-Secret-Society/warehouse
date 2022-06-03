from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [set() for _ in range(numCourses)]
        out_degrees = [set() for _ in range(numCourses)]
        result = []
        for course, pre_course in prerequisites:
            in_degrees[course].add(pre_course)
            out_degrees[pre_course].add(course)
        stack = []
        for i in range(numCourses):
            if not in_degrees[i]:
                stack.append(i)
        while stack:
            current_course = stack.pop()
            for next_course in out_degrees[current_course]:
                in_degrees[next_course].remove(current_course)
                if not in_degrees[next_course]:
                    stack.append(next_course)
            result.append(current_course)

        return result if len(result) == numCourses else []


print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
