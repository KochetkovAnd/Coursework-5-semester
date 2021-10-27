from sympy import *

def method_chord(fn, x0, x1, e):

    expr = sympify(fn)
    f = lambdify("x", expr)

    x, xPrev = x1, x0
    Xs = []
    Xs.append((0, x, abs(xPrev - x)))
    i = 1 
    while abs(x - xPrev) > e and i < 50000: 
        x, xPrev =  x - f(x) * (x - xPrev) / (f(x) - f(xPrev)), x
        Xs.append((i, x, abs(xPrev - x)))   
        i += 1 
    if(i == 500):
        return "Корней нет или задана слишком малая погрешность", []
    return x, Xs

def checkFor(fn, x0, x1):
    expr = sympify(fn)
    f = lambdify("x", expr)
    return f(x0) >= 0 and f(x1) < 0 or f(x1) >= 0 and f(x0) < 0

print(method_chord("x^3 - 1 ", 0 , 2 , 0.0001)[0])