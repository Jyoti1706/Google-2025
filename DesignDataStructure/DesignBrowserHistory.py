class BrowserHistoryViaList:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current+1] + [url]
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history)-1, self.current + steps)
        return self.history[self.current]


class BrowserHistoryViaStack:

    def __init__(self, homepage: str):
        self.prev = []
        self.next = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.prev.append(self.curr)
        self.curr = url
        self.next = []

    def back(self, steps: int) -> str:
        while steps != 0 and self.prev:
            self.next.append(self.curr)
            self.curr = self.prev[-1]
            self.prev.pop()
            steps -= 1
        return self.curr

    def forward(self, steps: int) -> str:
        while steps != 0 and self.next:
            self.prev.append(self.curr)
            self.curr = self.next[-1]
            self.next.pop()
            steps -= 1
        return self.curr

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)