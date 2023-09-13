from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1

        candies = []
        if ratings[0] > ratings[1]:
            candies.append(0)
        else:
            candies.append(1)
        for i in range(1,len(ratings)-1):
            if ratings[i-1] >= ratings[i] and ratings[i] <= ratings[i+1]:
                candies.append(1)
            elif ratings[i-1] <= ratings[i] and ratings[i] >= ratings[i+1]:
                candies.append(-1)
            else:
                candies.append(0)

        if ratings[-2] >= ratings[-1]:
            candies.append(1)
        else:
            candies.append(0)

        i = 0
        while i < len(candies):
            if candies[i] == -2:
                candies[i] = 1
            elif candies[i] == 1:
                j = i - 1
                cur_candy = 2
                while j >= 0:
                    if candies[j] != 0:
                        break
                    candies[j] = cur_candy
                    cur_candy += 1
                    j -= 1
                j = i + 1
                cur_candy = 2
                while j < len(ratings):
                    if candies[j] != 0:
                        i = j - 1
                        break
                    candies[j] = cur_candy
                    cur_candy += 1
                    j += 1
            i += 1
        for i in range(1, len(ratings)-1):
            if candies[i] == -1:
                if candies[i+1] == -1:
                    candies[i] = candies[i-1] + 1
                    candies[i+1] = candies[i+2] + 1
                else:
                    candies[i] = max(candies[i-1], candies[i+1]) + 1

        return sum(candies)

print(Solution().candy([1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]))