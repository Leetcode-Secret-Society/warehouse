from collections import deque

class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = [1]
        else:
            self.nums.append(self.nums[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.nums):
            return 0
        else:
            return self.nums[-1] // self.nums[-k-1]
# Your ProductOfNumbers object will be instantiated and called as such:

input1 = ["add","add","add","getProduct","add","add","add","getProduct","getProduct","getProduct","add","add"]
input2 = [[0],[0],[9],[3],[8],[3],[8],[5],[4],[6],[8],[8]]

obj = ProductOfNumbers()
for i in range(len(input1)):
    print(getattr(obj, input1[i])(input2[i][0]))
