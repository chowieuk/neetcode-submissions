
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*' , '/'}
        stack = []
        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                match token:
                    case '+':
                        stack.append(b + a)
                    case '-':
                        stack.append(b - a)
                    case '*':
                        stack.append(b * a)
                    case '/':
                        stack.append(int(float(b) / float(a)))
            else:
                stack.append(int(token))
        return stack[-1]