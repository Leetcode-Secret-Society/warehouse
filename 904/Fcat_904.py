from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first_fruit = fruits[0]
        second_fruit = None
        i = 1
        fruit_count = 1
        max_fruit = 1
        last_diff_index = 0
        while i < len(fruits):
            if fruits[i] != first_fruit:
                if second_fruit is None:
                    second_fruit = fruits[i]
                    last_diff_index = i
                elif fruits[i] != second_fruit:
                    first_fruit = fruits[last_diff_index]
                    second_fruit = fruits[i]
                    max_fruit = max(max_fruit, fruit_count)
                    i = last_diff_index
                    fruit_count = 0
                elif fruits[i] != fruits[i-1]:
                    last_diff_index = i
            fruit_count += 1
            i+=1

        max_fruit = max(max_fruit, fruit_count)
        return max_fruit
print(Solution().totalFruit([1,2,1]))
print(Solution().totalFruit([0,1,2,2]))
print(Solution().totalFruit([1,2,3,2,2]))
print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))