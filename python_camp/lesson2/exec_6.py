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
    for item in number :
        result = result + int(item)

        	

if __name__ == "__main__":
    print calculator('+', 10 , 100, 2)