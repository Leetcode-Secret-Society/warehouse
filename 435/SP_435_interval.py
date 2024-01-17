class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        k = -sys.maxsize - 1


        '''
    y4>...>y1
    Xs is non-ordered
    [x1]
     k
     V
    -inf x1----------y1
                x2-----------------y2
            x3---------------------------y3
        #k = y1
    [x2]

                    k
                    V
        x1----------y1
                x2-----------------y2
            x3---------------------------y3
        #count+=1 (overlapped)
    [x3]
                    k
                    V
        x1----------y1
                x2-----------------y2
            x3---------------------------y3
        #count+=1 (overlapped)


    [x4]
                    k
                    V
        x1----------y1
                x2-----------------y2
            x3---------------------------y3
                        x4-------------------y4
        #k=y4 
        '''
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                count += 1
        
        return count

