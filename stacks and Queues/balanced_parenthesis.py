from collections import deque

def check_pair(val1,val2):
    return (val1 == '(' and val2 == ')') or (val1 == '[' and val2 == ']') or (val1 == '{' and val2 == '}')

def balanced(expr):
    n = len(expr)
    stack = deque()

    for i in range(0,n):
        #when opening brackets.
        if expr[i] == '(' or expr[i] == '{' or expr[i] == '[':
            stack.append(expr[i])
        else:
            if len(stack) == 0:
                return False
            elif check_pair(stack[-1],expr[i]):
                stack.pop()
                continue
            return False
    return True


expr = "()(){([])()}"
if balanced(expr):
    print('Balanced')
else:
    print('Not Balanced')