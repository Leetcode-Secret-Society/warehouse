class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current_index+1]
        self.history.append(url)
        self.current_index += 1

    def back(self, steps: int) -> str:
        current_index = max(self.current_index-steps, 0)
        self.current_index = current_index
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        current_index = min(self.current_index + steps, len(self.history) - 1)
        self.current_index = current_index
        return self.history[self.current_index]
