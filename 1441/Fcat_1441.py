from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_index = 0
        current_n = 1
        result = []
        while target_index < len(target):
            result.append("Push")
            if target[target_index] == current_n:
                target_index += 1
            else:
                result.append("Pop")
            current_n += 1
        return result
