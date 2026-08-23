class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token == "+":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 + val2)
            elif token == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 - val2)
            elif token == "*":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 * val2)
            elif token == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1 / val2))
            else:
                stack.append(int(token))
        
        return stack.pop()
