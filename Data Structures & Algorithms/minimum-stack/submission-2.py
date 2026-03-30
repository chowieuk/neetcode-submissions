class MinStack:

    def __init__(self):
        self.store = []
        self.minStore = [math.inf]
        self.length = 0

    def push(self, val: int) -> None:
        self.store.append(val)
        self.minStore.append(min(val,self.minStore[-1]))

    def pop(self) -> None:
        self.store.pop()
        self.minStore.pop()        

    def top(self) -> int:
        return self.store[-1]

    def getMin(self) -> int:
        return self.minStore[-1]
        
