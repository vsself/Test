"""
design an function to implement factorial value.
e.g.
factorial(5)=5*4*3*2*1=120
"""

def factorial(num1):
    if num1 == 1:
        return num1
    else:
        return num1*factorial(num1-1)

if __name__ == "__main__":
    print factorial(5)
     