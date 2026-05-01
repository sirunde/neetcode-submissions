class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)

            else:
                if stack:
                    if i == ']':
                        if stack.pop() == '[':
                            continue
                        else:
                            return False
                    elif i == ')':
                        if stack.pop() == '(':
                            continue
                        else:
                            return False
                    else:
                        if stack.pop() == '{':
                            continue
                        else:
                            return False
                else:
                    return False
        if stack:
            return False
        return True
            
