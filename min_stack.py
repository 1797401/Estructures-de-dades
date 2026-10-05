class MinStack:

    def __init__(self):
        self.pila=list()
        self.minims=list()

    def push(self, val: int) -> None:
        self.pila.append(val)
        if len(self.minims)==0:
            self.minims.append(val)
        else:
            if val<=self.minims[-1]:
                self.minims.append(val)

    def pop(self) -> None:
        ultim=self.pila.pop()
        if ultim==self.minims[-1]:
            self.minims.pop()
        

    def top(self) -> int:
        return self.pila[-1]

    def getMin(self) -> int:
        return self.minims[-1]
