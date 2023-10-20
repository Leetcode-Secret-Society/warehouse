from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        def count_books(i, length):
            book_count = (2 * books[i] - length + 1) * length // 2
            return book_count

        dp = [0] * len(books)
        stack = []
        for i in range(len(books)):
            while stack and books[stack[-1]] - stack[-1] > books[i] - i:
                stack.pop()

            if stack:
                dp[i] = count_books(i, i - stack[-1]) + dp[stack[-1]]
            else:
                dp[i] = count_books(i, min(books[i], i+1))

            stack.append(i)

        return max(dp)


print(Solution().maximumBooks([8, 2, 3, 7, 3, 4, 0, 1, 4, 3]))
