

#here goes the code

def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.

    poly: list of numbers, length > 0
    x: number
    returns: float
    '''

    i=0.0
    tot=0.0
    for number in poly:
        s=0.0
        m=1.0
        j=0.0
        while(j<i):
            m=m*x
            j=j+1
        i=i+1
        s=number*m
        tot=tot+s
    return tot


print evaluatePoly([0,0,5, 9.3, 7], -13.0)
