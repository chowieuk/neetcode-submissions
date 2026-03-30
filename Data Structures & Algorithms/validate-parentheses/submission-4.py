class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False
        leftStack = []
        rightStack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                leftStack.append(c)
            else:
                rightStack.append(c)
                if len(leftStack) < 1: return False
                candidate = leftStack.pop()
                if (candidate == '(' and c == ')') or (candidate == '{' and c == '}') or (candidate == '[' and c == ']'):
                    rightStack.pop()
                    continue
                else:
                    return False
        return len(leftStack) == len(rightStack)
