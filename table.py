from functions import *

def Table(equation, start, end, step):
    if equation != '':
        eqa = ReplaceSymbol(equation)
        lst = []
        i = start - step
        while i <= (end-step):
            i += step
            lst.append(strfNumber(round(Calc(eqa, i),12)))
        return lst
    else:
        lst = []
        i = start - step
        while i <= (end-step):
            i += step
            lst.append('')
        return lst

def makeString(Obj):
    if Obj == '':
        result = ''
    elif len(Obj) <= 25:
        result = Obj.replace('e+', ' x 10^').replace('e', ' x 10^')
    else:
        Obj = eval(Obj)
        if Obj >= 10**25:
            ilg = len(str(int(Obj))) - 1
            result = str(round(Obj/(10**ilg), (17-len(str(ilg))))) + ' x 10^' + str(ilg)
    return result + (25-len(result))*' '


if __name__ == "__main__":
    fx = input('f(x) = ')
    gx = input('g(x) = ')
    hx = input('h(x) = ')
    start = eval(input('Start:\t'))
    end = eval(input('End:\t'))
    try:
        step = eval(input('Step:\t'))
        assert step!=0, "Step cannot be 0 !!!"
    except AssertionError as err:
        print(err)

    x = Table("x", start, end, step)
    lst_fx = Table(fx, start, end, step)
    lst_gx = Table(gx, start, end, step)
    lst_hx = Table(hx, start, end, step)
    lst_result = [x, lst_fx, lst_gx, lst_hx]

    print('╭─────────────────────────┬─────────────────────────┬─────────────────────────┬─────────────────────────╮')
    print('│            x            │           f(x)          │           g(x)          │           h(x)          │')
    print('├─────────────────────────┼─────────────────────────┼─────────────────────────┼─────────────────────────┤')
    for j in range(0, len(x)):
        print('│' + makeString(lst_result[0][j]) + '│' + makeString(lst_result[1][j]) + '│' + makeString(lst_result[2][j]) + '│' + makeString(lst_result[3][j]) + '│')
        if j == len(x) - 1:
            print('╰─────────────────────────┴─────────────────────────┴─────────────────────────┴─────────────────────────╯')
        else:
            print('├─────────────────────────┼─────────────────────────┼─────────────────────────┼─────────────────────────┤')
