class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        result = [['.'] * len(box) for i in range(len(box[0]))]
        for y in range(len(box)):
            obstacle_indexes = []
            stone_count = [0]
            for x in range(len(box[0])):
                if box[y][x] == '#':
                    stone_count[-1] += 1
                elif box[y][x] == '*':
                    obstacle_indexes.append(x)
                    stone_count.append(0)
            for index, stone_index in enumerate(obstacle_indexes):
                result[stone_index][len(box) - 1 - y] = '*'
                for i in range(stone_count[index]):
                    result[stone_index - i - 1][len(box) - 1 - y] = '#'
            for i in range(stone_count[-1]):
                result[-1 - i][len(box) - 1 - y] = '#'

        return result