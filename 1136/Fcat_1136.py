class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        prev_courses = [0] * (n+1)
        next_courses = [[] for i in range(n+1)]
        for p, nex in relations:
            prev_courses[nex] += 1
            next_courses[p].append(nex)

        finished_course = set()
        semesters = 0
        while True:
            this_semester_courses = []
            for i in range(1, n + 1):
                if i not in finished_course and prev_courses[i] == 0:
                    this_semester_courses.append(i)
                    finished_course.add(i)
            if len(this_semester_courses) == 0:
                if len(finished_course) == n:
                    return semesters
                else:
                    return -1
            semesters += 1
            for i in this_semester_courses:
                for nex in next_courses[i]:
                    prev_courses[nex] -= 1