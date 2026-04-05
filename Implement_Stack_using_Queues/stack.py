class Queue:
    def __init__(self):
        self.items = []
    def push(self, x: int) -> None:
        self.items.append(x)


    def pop(self) -> int:
        return self.items.pop(0)

    def peek(self) -> int:
        return self.items[0]

    def empty(self) -> bool:
        return len(self.items) == 0

class MyStack:

    def __init__(self):
        self.stk = Queue()
        self._top = None
        self.size = 0

    def push(self, x: int) -> None:
        self.stk.push(x)
        self._top = x
        self.size += 1

    def pop(self) -> int:
        for _ in range(self.size - 1):
            self._top = self.stk.peek()
            self.stk.push(self.stk.pop())
        self.size -= 1
        return self.stk.pop()

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return self.stk.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
