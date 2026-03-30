class Logger:

    def __init__(self):
        self.lastPrinted = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.lastPrinted:
            if self.lastPrinted[message] > timestamp - 10:
                return False
        self.lastPrinted[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
