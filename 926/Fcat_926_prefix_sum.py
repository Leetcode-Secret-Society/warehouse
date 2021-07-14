class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix = [0]
        one_count = 0
        for d in s:
            if d == '1':
                one_count += 1
            prefix.append(one_count)

        return min(prefix[i] + len(s) - i - 1 - (prefix[-1] - prefix[i + 1]) for i in range(len(s)))


print(Solution().minFlipsMonoIncr("10011111110010111011"))
