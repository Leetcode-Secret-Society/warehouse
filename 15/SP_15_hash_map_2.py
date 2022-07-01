class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        postives = {}
        zeros = {}
        negitives = {}
        result = set()
        
        for num in nums:
            if num > 0:
                postives[num] = postives.get(num, 0) + 1
            elif num < 0:
                negitives[num] = negitives.get(num, 0) + 1
            else:
                zeros[num] = zeros.get(num, 0) + 1

        len_zeros = zeros.get(0, 0)
        # -x , 0 , +x
        if len_zeros > 0:
            for pos in postives.keys():
                if pos * -1 in negitives.keys():
                    result.add((pos * -1, 0 , pos))
        if len_zeros >= 3:
            result.add((0, 0, 0))
        # i, x, y;  i + x + y = 0, x and y must be all postive or negitive
        for pos in postives.keys():
            for neg in negitives.keys():
                if pos + neg > 0 and -1 * (pos + neg) in negitives.keys():
                    result.add(tuple(sorted([pos, neg, -1 * (pos + neg)])))
                elif pos + neg < 0 and -1 * (pos + neg) in postives.keys():
                    result.add(tuple(sorted([pos, neg, -1 * (pos + neg)])))

        sets_to_remove = set()
        for r in result:
            num_used = {}
            for ele in r :
                num_used[ele] = num_used.get(ele, 0)+1
            for num in num_used.keys():
                count = max(postives.get(num, 0), negitives.get(num, 0), zeros.get(num, 0))
                if num_used[num] > count:
                    sets_to_remove.add(r)
        for to_remove in sets_to_remove:
            result.remove(to_remove)
        
        return result
        
        
