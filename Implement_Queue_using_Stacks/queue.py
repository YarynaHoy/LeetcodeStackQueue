class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MyQueue:

    def __init__(self):
        self.in_q = Stack()
        self.out_q = Stack()

    def push(self, x: int) -> None:
        self.in_q.push(x)

    def pop(self) -> int:
        if self.out_q.empty():
            while not self.in_q.empty():
                self.out_q.push(self.in_q.pop())
        return self.out_q.pop()

    def peek(self) -> int:
        if self.out_q.empty():
            while not self.in_q.empty():
                self.out_q.push(self.in_q.pop())
        return self.out_q.top()

    def empty(self) -> bool:
        return self.in_q.empty() and self.out_q.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
