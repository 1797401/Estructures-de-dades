class MinStack:

    def __init__(self):
        self.stack=list()
        self.minims=list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<=self.minims[:-1]:
            self.minims.append(val)

    def pop(self) -> None:
        ultim=self.stack.pop()
        if ultim==self.minims[:-1]:
            self.minims.pop()
        

    def top(self) -> int:
        return self.stack[:-1]

    def getMin(self) -> int:
        return self.minims[:-1]
