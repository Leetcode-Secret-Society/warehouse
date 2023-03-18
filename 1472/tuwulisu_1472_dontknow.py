class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr = 0
        self.top = 0
        

    def visit(self, url: str) -> None:
        self.curr+=1
        self.top=self.curr
        if self.top>=len(self.stack):
            self.stack.append(url)
        else:
            self.stack[self.top] = url

    def back(self, steps: int) -> str:
        self.curr = max(self.curr-steps, 0)
        return self.stack[self.curr]
        

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr+steps, self.top)
        return self.stack[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
