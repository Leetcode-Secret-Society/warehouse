import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def get_element(array, index):
            if 0 <= index <= len(array):
                return array[index-1]
            else:
                return -1
        n_sqrt = int(math.sqrt(n))
        result_a = []
        result_b = []
        for i in range(1, n_sqrt+1):
            if n % i == 0:
                result_a.append(i)
                result_b.append(n//i)
        if result_a[-1] * result_a[-1] == n:
            result_a.pop()
        result = result_a + result_b[::-1]
        return get_element(result, k)
