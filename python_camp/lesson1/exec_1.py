"""
design an caculator for basic operation: +, -, *, /, and ...
"""


def caculator(num1, num2, method):
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

