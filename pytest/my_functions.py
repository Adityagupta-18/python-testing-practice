def add(num1,num2):
    return num1+num2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    if n2==0:
        raise ZeroDivisionError
    return n1/n2
