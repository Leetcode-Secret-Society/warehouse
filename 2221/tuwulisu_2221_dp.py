class Solution:
    def __init__(self):
        self.f_memo = {0:1}
        self.current_last = 0

    def factorial(self, n):
        if n in self.f_memo:
            return self.f_memo[n]
        else:
            current_f = self.f_memo[self.current_last]
            for i in range(self.current_last+1, n+1):
                current_f *= i
                self.f_memo[i] = current_f
            self.current_last = n
            return self.f_memo[n]

    def cal_pascal_triangle(self, n):
        pascal_triangle = []
        for i in range(n):
            ri = i+1
            pascal_triangle.append(self.factorial(n-1)//self.factorial(i)//self.factorial(n-i-1))
        return pascal_triangle
            
    def triangularSum(self, nums: List[int]) -> int:
        pascal_triangle = self.cal_pascal_triangle(len(nums))
        ans = sum([a*b for a,b in zip(nums, pascal_triangle)])%10
        return ans
