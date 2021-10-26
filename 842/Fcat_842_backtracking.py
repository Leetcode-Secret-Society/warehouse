from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def check_next_fib(fibs, index):
            while str(fibs[-1] + fibs[-2]) == num[index:index + len(str(fibs[-1] + fibs[-2]))]:
                if fibs[-1] + fibs[-2] >= 2147483648:
                    return False
                fibs.append(fibs[-1] + fibs[-2])
                index += len(str(fibs[-1]))
            return index == len(num)

        if num[0] == '0':
            second_len = 1
            while second_len <= len(num)//2:
                if 1+second_len == len(num):
                    return []
                result = [0, int(num[1:1+second_len])]
                if check_next_fib(result, 1+second_len):
                    return result
                second_len += 1
        else:
            first_len = 1
            while first_len <= len(num)//2:
                second_len = 1
                if num[first_len] == '0':
                    result = [int(num[0:first_len]), 0]
                    if check_next_fib(result, first_len+1):
                        return result
                    else:
                        first_len += 1
                        continue
                while second_len <= len(num)//2:
                    if first_len+second_len == len(num):
                        return []

                    result = [int(num[0:first_len]), int(num[first_len:first_len+second_len])]
                    if check_next_fib(result, first_len+second_len):
                        return result
                    second_len += 1
                first_len += 1

        return []



print(Solution().splitIntoFibonacci("1320581321313221264343965566089105744171833277577"))