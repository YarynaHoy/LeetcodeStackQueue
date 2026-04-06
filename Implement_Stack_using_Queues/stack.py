class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


    def pop(self) -> int:
        if not self.head:
            return None

        if self.head.next is None:
            val = self.head.value
            self.head = None
            self.size -= 1
            return val

        cur = self.head
        while cur.next.next:
            cur = cur.next

        val = cur.next.value
        cur.next = None
        self.size -= 1
        return val


    def peek(self) -> int:
        if not self.head:
            return None
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur.value

    def empty(self) -> bool:
        return self.head is None


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
