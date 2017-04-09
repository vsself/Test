"""
design an caculator for basic operation: +, -, *, /, and ()
e.g.
calculator('3+2-4')
calculator('3+2*4')
calculator('(3+2)*4')
calculator('(3+2)/4')
"""

def calculator(expression):
    list1 = []
    flag = 0
    length = len(expression)
    for i in range(length):       
        if expression[i] == '(':
            if (i-1 >= 0) & number(expression[i-1]):
                list1.append('*')
                list1.append('(')
            else:
                list1.append('(')
        elif expression[i] == ')':
            if (i+1 < length) & number(expression[i+1]):
                list1.append(')')
                flag = 1
            else:
                list1.append(')')
        else:
            if flag ==  1:
                flag = 0
                list1.append('*')
                list1.append(expression[i])
            else:
                list1.append(expression[i])
    print list1
    result = loop(list1)               
    print result
    return float(result)



def loop(list1):
    length = len(list1)
    print 'length = %d'  %length
    if length == 1:
        return list1[0]
    for i in range(length):
        if number(list1[i]):
            if ((i+2) < length) & number(list1[i+2]):
                if i+2 == (length-1):
                    list1[i] = str(calc(list1[i], list1[i+2], list1[i+1]))
                    list1.pop(i+1)
                    list1.pop(i+1)
                    print list1
                    return loop(list1)
                elif (list1[i+3] == ')') | (priority(list1[i+1]) >= priority(list1[i+3])):
                    list1[i] = str(calc(list1[i], list1[i+2], list1[i+1]))
                    list1.pop(i+1)
                    list1.pop(i+1)
                    print list1
                    return loop(list1)
                else:
                    continue
            elif (i+1 < length) & (i-1 >= 0) & (list1[i-1] == '(') & (list1[i+1] == ')'):
                list1[i-1] = list1[i]
                list1.pop(i)
                list1.pop(i)
                print list1
                return loop(list1)
        else:
            continue
                            
        
def number(string1):
    if string1 == '+':
        return False
    if string1 == '-':
        return False
    if string1 == '/':
        return False
    if string1 == '*':
        return False
    if string1 == '(':
        return False
    if string1 == ')':
        return False
    return True
    
def calc(num1, num2, method):
    dignum1 = float(num1)
    dignum2 = float(num2)
    if method == '+':
        result = dignum1 + dignum2
    elif method == '-':
        result = dignum1 - dignum2
    elif method == '*':
        result = dignum1 * dignum2
    else:
        if dignum2 != 0:
            result = dignum1/dignum2
        else:
            result = None
    return result

def priority(string1):
    if (string1 == '-') | (string1 == '+'):
        return 1
    else:
        return 2
    
if __name__ == "__main__":
    print calculator('2(3+(2-4)/2)5')

     
#