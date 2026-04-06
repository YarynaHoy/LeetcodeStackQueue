class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if not self.head:
            return None
        val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return val

    def top(self):
        return self.head.value if self.head else None

    def empty(self):
        return self.size == 0

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
