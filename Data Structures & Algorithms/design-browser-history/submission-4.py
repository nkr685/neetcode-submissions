class ListNode:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode("")
        self.tail = ListNode("")
        self.curr = ListNode(homepage)
        self.curr.next = self.tail
        self.curr.prev = self.head
        self.head.next = self.curr
        self.tail.prev = self.curr

    def visit(self, url: str) -> None:
        node, next, prev = ListNode(url), self.tail, self.curr if self.curr else self.head
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node
        self.curr = node

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.curr.prev == self.head:
                break
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        if not self.curr:
            return "none"
        while steps > 0:
            if self.curr.next == self.tail:
                break
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)