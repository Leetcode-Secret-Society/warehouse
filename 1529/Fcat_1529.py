class Solution:
    def minFlips(self, target: str) -> int:
        state = "0"
        flip_count = 0
        for bit in target:
            if bit != state:
                flip_count += 1
                state = bit
        return flip_count
