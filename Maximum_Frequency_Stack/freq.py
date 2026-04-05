from collections import defaultdict, deque

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.val = defaultdict(deque)
        self.max_v = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]

        self.max_v = max(self.max_v, f)

        self.val[f].append(val)

    def pop(self) -> int:
        res = self.val[self.max_v].pop()

        self.freq[res] -= 1

        if not self.val[self.max_v]:
            self.max_v -= 1

        return res
