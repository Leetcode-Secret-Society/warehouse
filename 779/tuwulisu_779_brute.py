class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [poured]
        for current_row in range(query_row):
            next_row = [0]*(len(row)+1)
            for i in range(len(row)):
                if row[i]>1:
                    next_row[i]+=(row[i]-1)/2
                    next_row[i+1]+=(row[i]-1)/2
            row=next_row
        return row[query_glass] if row[query_glass]<1 else 1