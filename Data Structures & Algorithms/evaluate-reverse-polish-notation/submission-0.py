class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:

            if token == "+":
                a = stack.pop()
                b = stack.pop()
                temp = a+b

                stack.append(temp)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()

                temp = b-a
                stack.append(temp)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                temp = a*b

                stack.append(temp)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                temp = int(b/a)
                stack.append(temp)
            else:
                stack.append(int(token))
        return stack[-1]
