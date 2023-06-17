class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        r = maxSum + 1
        l = 1
        while l < r:
            mid = (l + r) // 2
            if self.count_sum(n, index, mid) <= maxSum:
                l = mid + 1
            else:
                r = mid
        return l - 1

    def count_sum(self, n, index, max_value):
        if max_value > index:
            left = ((max_value - index) + max_value) * (index + 1) // 2
        else:
            left = (1 + max_value) * max_value // 2 + (index - max_value + 1)

        if max_value >= n - index:
            right = ((max_value - (n - index - 1)) + max_value) * (n - index) // 2
        else:
            right = (1 + max_value) * max_value // 2 + (n - index - max_value)

        return left + right - max_value