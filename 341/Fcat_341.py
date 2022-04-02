class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.stack = [[nestedList, 0]]
        while self.stack and not self.stack[-1][0][self.stack[-1][1]].isInteger():
            if self.stack[-1][0][self.stack[-1][1]].getList():
                self.stack.append([self.stack[-1][0][self.stack[-1][1]].getList(), 0])
            else:
                self.stack[-1][1] += 1
                while self.stack and self.stack[-1][1] == len(self.stack[-1][0]):
                    self.stack.pop()
                    if self.stack:
                        self.stack[-1][1] += 1

    def next(self) -> int:
        value = self.stack[-1][0][self.stack[-1][1]].getInteger()
        self.stack[-1][1] += 1
        while self.stack and self.stack[-1][1] == len(self.stack[-1][0]):
            self.stack.pop()
            if self.stack:
                self.stack[-1][1] += 1
        while self.stack and not self.stack[-1][0][self.stack[-1][1]].isInteger():
            if self.stack[-1][0][self.stack[-1][1]].getList():
                self.stack.append([self.stack[-1][0][self.stack[-1][1]].getList(), 0])
            else:
                self.stack[-1][1] += 1
                while self.stack and self.stack[-1][1] == len(self.stack[-1][0]):
                    self.stack.pop()
                    if self.stack:
                        self.stack[-1][1] += 1
        return value

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
