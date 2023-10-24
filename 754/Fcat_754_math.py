class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        i = 0
        total = 0
        while total < target:
            i += 1
            total += i
        if total == target or (total - target) % 2 == 0:
            return i
        else:
            i += 1
            if i % 2 == 0:
                i += 1
            return i
