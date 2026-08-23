class MinStack:

    def __init__(self):
        self.diffstack = deque()
        self.cur_min = 0 # at init, means nothing

    def push(self, val: int) -> None:
        if self.diffstack:
            self.diffstack.append(val - self.cur_min)
            self.cur_min = min(val, self.cur_min)
        else:
            self.diffstack.append(0)
            self.cur_min = val

    def pop(self) -> None:
        if self.diffstack[-1] < 0:
            self.cur_min -= self.diffstack.pop()
        else:
            self.diffstack.pop()
        

    def top(self) -> int:
        if self.diffstack[-1] >= 0:
            return self.diffstack[-1] + self.cur_min
        else:
            return self.cur_min
        

    def getMin(self) -> int:
        return self.cur_min
        
