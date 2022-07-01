class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        postives = []
        zeros = []
        negitives = []
        result = set()
        
        for num in nums:
            if num > 0:
                postives.append(num)
            elif num < 0:
                negitives.append(num)
            else:
                zeros.append(num)

        pos_set = set(postives)
        neg_set = set(negitives)
        # -x , 0 , +x
        if len(zeros) > 0:
            for pos in pos_set:
                if pos * -1 in neg_set:
                    result.add((pos * -1, 0 , pos))
        if len(zeros) >= 3:
            result.add((0, 0, 0))
        # i, x, y;  i + x + y = 0,
        # list all posibilities, must be postive, postive, negitive or postive, negitive, negitive
        for x_index in range(len(postives)): 
            for y_index in range(x_index+1,len(postives)):
                x = postives[x_index]
                y = postives[y_index]
                if -1 * (x + y) in neg_set:
                    result.add(tuple(sorted([-1 * (x + y), x , y])))
        for x_index in range(len(negitives)): 
            for y_index in range(x_index+1,len(negitives)):
                x = negitives[x_index]
                y = negitives[y_index]
                if -1 * (x + y) in pos_set:
                    result.add(tuple(sorted([-1 * (x + y), x , y])))
        return result
