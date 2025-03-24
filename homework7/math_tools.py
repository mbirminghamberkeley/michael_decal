def add(a,b):
    '''
    returns the sum of a and b
    '''
    return a+b

def subtract(a,b):
    '''
    returns the difference of a and b
    '''
    return a-b

def multiply(a,b):
    '''
    returns the product of a and b
    '''
    return a*b

def divide(a,b):
    '''
    returns the quotient of a and b, handling division by 0
    '''
    if b == 0:
        return "Error: Division by 0"
    else:
        return a/b