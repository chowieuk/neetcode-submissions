class MinStack:

    def __init__(self):
        self.elements = []
        self.min = []

    def push(self, val: int) -> None:
        self.elements.append(val)
        self.min.append(val) if len(self.min) == 0 else self.min.append(min(self.min[-1], val))
        print(self.elements)
        print(self.min)

    def pop(self) -> None:
        self.elements.pop()
        self.min.pop()
        
    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.min[-1]