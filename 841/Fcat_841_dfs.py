from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        path = [0]
        walked = set(path)
        for connect_rooms in path:
            for room in rooms[connect_rooms]:
                if room not in walked:
                    walked.add(room)
                    path.append(room)
        return len(walked) == len(rooms)
print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))