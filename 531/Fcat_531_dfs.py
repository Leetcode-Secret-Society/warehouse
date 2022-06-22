from typing import List

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        b_column = [False] * len(picture)
        b_row = [False] * len(picture[0])
        result = 0
        for y in range(len(picture)):
            if b_column[y]:
                continue
            for x in range(len(picture[0])):
                if b_row[x]:
                    continue
                if picture[y][x] == "B":
                    b_row[x] = True
                    b_column[y] = True
                    hit = False
                    for column in range(len(picture)):
                        if column == y:
                            continue
                        if picture[column][x] == 'B':
                            hit = True
                            break
                    if not hit:
                        for row in range(len(picture[0])):
                            if row == x:
                                continue
                            if picture[y][row] == 'B':
                                hit = True
                                break
                    if not hit:
                        result += 1
        return result

print(Solution().findLonelyPixel([["W","W","B"]]))