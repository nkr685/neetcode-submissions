class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.tail = self.head
        self.current = self.head

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.current.next = node
        node.prev = self.current
        self.current = node
        self.tail = node

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.current.prev:
                break
            else:
                self.current = self.current.prev
        return self.current.val


    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.current.next:
                break
            else:
                self.current = self.current.next
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)