class Solution:
    def countOrders(self, n: int) -> int:
        last_result = 1
        for i in range(2, n+1):
            last_result = (2*i-1) * last_result + ((2*i-1) * (2*i-2)//2) * last_result
        return last_result % (pow(10,9) + 7)

