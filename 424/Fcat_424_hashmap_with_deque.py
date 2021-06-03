# Definition for a binary tree node.
from collections import defaultdict
from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_repeat_length = defaultdict(int)
        alphabet_distribute = defaultdict(list)
        for i in range(len(s)):
            alphabet_distribute[s[i]].append(i)

        for alphabet, distribute in alphabet_distribute.items():
            total_interval = 0
            current_positions = deque()

            for pos in distribute:
                if current_positions:
                    if total_interval + pos - current_positions[-1] > k:
                        max_repeat_length[alphabet] = max(max_repeat_length[alphabet], current_positions[-1] - current_positions[0] + 1 + k - total_interval)

                    total_interval += pos - current_positions[-1] - 1
                current_positions.append(pos)
                while total_interval > k:
                    left = current_positions.popleft()
                    total_interval -= current_positions[0] - left - 1
            max_repeat_length[alphabet] = max(max_repeat_length[alphabet], current_positions[-1] - current_positions[0] + 1 + k - total_interval)

        return min(max(max_repeat_length.values()), len(s))


print(Solution().characterReplacement('AABABBA', 1))