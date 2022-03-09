from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        obstacles = []
        stones = []
        for y in range(len(box)):
            obstacle_indexes = []
            stone_count = [0]
            for x in range(len(box[0])):
                if box[y][x] == '#':
                    stone_count[-1] += 1
                elif box[y][x] == '*':
                    obstacle_indexes.append(x)
                    stone_count.append(0)

            obstacles.append(obstacle_indexes)
            stones.append(stone_count)

        result = [['.'] * len(box) for i in range(len(box[0]))]
        for x in range(len(obstacles)):
            for index, stone_index in enumerate(obstacles[x]):
                result[stone_index][len(obstacles) - 1 - x] = '*'
                for i in range(stones[x][index]):
                    result[stone_index - i - 1][len(obstacles) - 1 - x] = '#'
            for i in range(stones[x][-1]):
                result[-1 - i][len(obstacles) - 1 - x] = '#'
        return result


Solution().rotateTheBox([["#","#","*",".","*","."],
                         ["#","#","#","*",".","."],
                         ["#","#","#",".","#","."]])