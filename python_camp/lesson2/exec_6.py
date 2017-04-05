"""
design an caculator for multiple numbers' basic operation: +, -, *, /, and ...
e.g:
calculator('+', 10, 100, 2)
calculator('-', 10, 100, 2)
calculator('*', 10, 100, 2)
calculator('/', 100, 10, 2)
"""


def calculator(method, *number):
    result = 0
    flag = True
    if method == '+':
        for item in number :
            if flag:
                result = int(item)
                flag = False
            else:
                result = result + int(item)
    elif method == '-':
        for item in number :
            if flag:
                result = int(item)
                flag = False
            else:
                result = result - int(item)                   	
    elif method == '*':
        for item in number :
            if flag:
                result = int(item)
                flag = False
            else:
                result = result * int(item)
                
    else:
        for item in number :
            if flag:
                result = float(item)
                flag = False
            else:
                result = result / float(item)
    return result
if __name__ == "__main__":
    print calculator('+', 10 , 100, 2)