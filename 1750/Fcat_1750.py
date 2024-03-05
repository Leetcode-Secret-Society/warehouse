class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        while left < right:
            target = s[left]
            if s[right] != target:
                break
            next_left = left + 1
            while next_left < len(s) and s[next_left] == target:
                next_left += 1
            if next_left >= len(s):
                if left == right:
                    return 1
                else:
                    return 0
            next_right = right - 1
            while s[next_right] == target:
                next_right -= 1
            if next_right < next_left:
                return 0
            left = next_left
            right = next_right

        return right - left + 1
