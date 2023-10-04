from collections import deque

class Solution:

    def maximumBooks(self, books: List[int]) -> int:
        def bruteForce(books) -> int: #TLE
            result = 0
            for i in range(len(books)):
                current = books[i]
                current_sum = current
                for j in range(i-1,-1,-1):
                    #note that 1. contiguous 2. decreasing
                    before_current = min(books[j], current - 1)
                    if before_current < 1: #end if 0
                        break
                    current_sum += before_current
                    current = before_current
                result = max(result, current_sum)
            return result

        def bruteForceDP(books) -> int: #TLE
            result = 0
            dp = [0] * len(books)
            for i in range(len(books)):
                current = books[i]
                current_sum = current
                for j in range(i-1,-1,-1):
                    #dp works if current larger than previous one
                    if books[j] <= current - 1:
                        current_sum += dp[j]
                        break
                        
                    #note that 1. contiguous 2. decreasing
                    before_current = min(books[j], current - 1)
                    if before_current < 1: #end if 0
                        break
                    current_sum += before_current
                    current = before_current
                result = max(result, current_sum)
                dp[i] = current_sum
            return result
        def monoStackDP(books) -> int: #TLE
            result = 0
            dp = [0] * len(books)
            pain_point = [-1] * len(books)

            stack = deque()
            for i in range(len(books)-1, -1, -1):
                # books[stack[-1]] means previous one
                # stack[-1] - i means distance from current(i) to previous one (stack[-1])
                # books[i] + stack[-1] - i should equal to previous one if it is a perfect increasing order (0,1,2,3...), but still a increasing order
                
                while len(stack) > 0 and books[i] + stack[-1] - i < books[stack[-1]]:
                    pain_point[stack.pop()] = i
                stack.append(i)
            print(pain_point)

            #or says, the sum from 1 to n
            def triangleVolume(n: int) -> int:
                return (n+1) * n // 2

            for i in range(len(books)):
                current = books[i]
                current_sum = current
                if pain_point[i] == -1:
                    current_sum = triangleVolume(current)
                    if current - i - 1 > 0:
                        current_sum -= triangleVolume(current - i - 1)
                else :
                    current_sum = dp[pain_point[i]] + triangleVolume(current) - triangleVolume(current - i + pain_point[i])
                dp[i] = current_sum
                result = max(current_sum, result)
            return result

        return monoStackDP(books)
