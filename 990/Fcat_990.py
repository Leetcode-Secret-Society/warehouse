from typing import List
from collections import defaultdict


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equal_mapping = {}
        not_equal_mapping = defaultdict(set)
        for equation in equations:
            if equation[1] == '!':
                left, right = equation.split('!=')
                if left == right:
                    return False
                not_equal_mapping[left].add(right)
            else:
                left, right = equation.split('==')
                if left not in equal_mapping and right not in equal_mapping:
                    equal_mapping[left] = {left,right}
                    equal_mapping[right] = equal_mapping[left]
                elif left not in equal_mapping:
                    equal_mapping[right].add(left)
                    equal_mapping[left] = equal_mapping[right]
                elif right not in equal_mapping:
                    equal_mapping[left].add(right)
                    equal_mapping[right] = equal_mapping[left]
                else:
                    equal_mapping[left].update(equal_mapping[right])
                    for c in equal_mapping[right]:
                        equal_mapping[c] = equal_mapping[left]
        for key, value in not_equal_mapping.items():
            for c in value:
                if c in equal_mapping.get(key, []):
                    return False
        return True


print(Solution().equationsPossible(["a==b","e==c","b==c","a!=e"]))