from sympy import diff, Symbol, lambdify
from sympy.parsing.sympy_parser import parse_expr

def abs(n):
    return n if n >= 0 else -n

def gcd(a, b):
    return gcd(abs(b), abs(a)) if a < b else abs(a) if b == 0 else gcd(abs(b), abs(a%b))

def lcm(a, b):
    return abs(a*b)/gcd(a, b)

def formatNumber(n):
    return int(n) if (n/1).is_integer() else n

def Derivative(equation, value):
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(equation, my_symbols)
    d_dx = diff(my_func, my_symbols['x'])
    result = lambdify(my_symbols['x'], d_dx)
    return result(value)

def Calc(equation, value):
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(equation, my_symbols)
    try:
        result = lambdify(my_symbols['x'], my_func)
        return result(value)
    except ZeroDivisionError:
        return 'error'

def ReplaceSymbol(equation):
    lst = [i for i in equation]
    for i in range(len(lst)):
        if lst[i] in 'xeπ':
            if (i-1) >= 0 and lst[i-1].isdigit():
                lst[i] = '*' + lst[i]
            if (i+1) <= (len(lst)-1):
                if lst[i+1].isdigit():
                    lst[i] += '*'
        elif lst[i] == '(':
            if (i-1) >= 0 and (lst[i-1] not in '+-*/^('):
                lst[i] = '*' + lst[i]
        elif lst[i] == ')':
            if (i+1) <= (len(lst)-1):
                if lst[i+1] not in '+-*/^)':
                    lst[i] += '*'
    return ''.join(lst).replace('^','**').replace('e','2.718281828459045').replace('π','3.141592653589793')
