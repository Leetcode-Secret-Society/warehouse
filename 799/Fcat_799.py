class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = []
        next_row = [poured]
        i = 0
        while True:
            current_row = next_row
            next_row = [0] * (len(current_row) + 1)
            have_overflow_glass = False
            for j in range(len(current_row)):
                if i == query_row and j == query_glass:
                    return min(1, current_row[j])
                if current_row[j] > 1:
                    next_row[j] += (current_row[j] - 1) / 2
                    next_row[j+1] += (current_row[j] - 1) / 2
                    have_overflow_glass = True
            if not have_overflow_glass:
                break
            i += 1

        return 0