from sympy import diff, Symbol, lambdify
from sympy.parsing.sympy_parser import parse_expr

gcd = lambda a, b: gcd(abs(b), abs(a)) if a < b else abs(a) if b == 0 else gcd(abs(b), abs(a%b))

lcm = lambda a, b: abs(a*b)/gcd(a, b)

strfNumber = lambda n: str(int(n)) if (n/1).is_integer() else str(n)

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

def horner(list_coefficient, x):
    list_result = [list_coefficient[0]]
    for i in range(len(list_coefficient)-1):
        result = x*list_result[i]+list_coefficient[i+1]
        list_result.append(result)
    return list_result

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
