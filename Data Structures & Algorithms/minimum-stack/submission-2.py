class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.getMin())))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        top_tuple = self.stack.pop()
        self.stack.append(top_tuple)
        return top_tuple[0]

    def getMin(self) -> int:
        top_tuple = self.stack.pop()
        self.stack.append(top_tuple)
        return top_tuple[1]
        
