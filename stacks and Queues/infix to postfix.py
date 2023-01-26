def precedence(ch, stack_top):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    try:
        a = prec[ch]
        b = prec[stack_top]

        return True if a <= b else False
    except KeyError:
        return False

def checkifoperand(a):
    return a.isalpha()

def convert(exp):
    s = []
    r = []

    for i in range(len(exp)):
        # print(r)
        # print(s)
        if checkifoperand(exp[i]):
            r.append(exp[i])
        
        elif exp[i] == '(':
            s.append(exp[i])
        
        elif exp[i] ==')':
            while len(s) > 0 and s[-1] != '(':
                r.append(s.pop())
            
            if len(s) >= 0 and s[-1] != '(':
                return -1
            else:
                s.pop()
        
        else:
            while len(s) > 0 and precedence(exp[i], s[-1]):
                r.append(s.pop())
            s.append(exp[i])

    while len(s) > 0:
        r.append(s.pop())
    
    return r


expression = "a+b*(c^d-e)^(f+g*h)-i"
arr = convert(expression)
print("".join(i for i in arr))