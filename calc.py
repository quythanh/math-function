from functions import *

print('Calculator')
fx = ReplaceSymbol(input(''))

while True:
    if 'x' not in fx:
        print(eval(fx))
        fx = ReplaceSymbol(input(''))
    else:
        cont = True
        while cont == True:
            x = input('x = ')
            if x != 'exit':
                x = eval(x)
                print(Calc(fx, x))
            else:
                cont = False
