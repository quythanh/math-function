from random import uniform
from datetime import datetime
from os import system
from functions import *

class Solve():
    def __init__(self, equation, x):
        self.equation = equation
        self.x = x

    def Check_form(self):
        stateList = self.equation.split('=')
        if len(stateList) == 2:
            if stateList[1] == '0':
                self.equation = stateList[0]
            elif stateList[1] == '':
                return False
            else:
                self.equation = stateList[0] + '-(' + stateList[1] + ')'
            self.equation.replace(' ','')
            return True
        return False

    def CheckSymbol(self):
        if self.Check_form() == False:
            return False

        self.equation = ReplaceSymbol(self.equation)

        return True

    def Solve(self):
        if self.CheckSymbol() == False:
            return False

        times = 0
        while Calc(self.equation, self.x) != 0 and times <= 20:
            times += 1
            derivative = Derivative(self.equation, self.x)
            if derivative != 0:
                self.x = round(self.x - Calc(self.equation, self.x)/derivative, 14)
            else:
                self.x += uniform(-3.0,3.0)
            if times == 20:
                if abs(Calc(self.equation, self.x)) < 10**-12 and abs(self.x) < 10**5:
                    return
                elif abs(Calc(self.equation, self.x)) < 10**-5 and abs(self.x) < 10**5:
                    print('x = \t', strfNumber(self.x))
                    print('L - R = ', strfNumber(Calc(self.equation, self.x)).replace('e+', ' x 10^').replace('e', ' x 10^'))

                    cont = input('Continue? (Y/N):\t')
                    if cont.lower() == 'y':
                        times = 0
                    else:
                        self.x = 'NaN'
                        return
                else:
                    self.x = 'NaN'
                    return
        if Calc(self.equation, self.x) == 0:
            return

def show_result(eqn, list_result, started_time):
    system('cls')
    print(eqn)

    for i in range(len(list_result)):
        if list_result[i] != 'NaN':
            print('x = \t', strfNumber(list_result[i]))
        else:
            print('Cannot Solve / The Equation Has No More Real Solution.')
    print('Solved in ',round((datetime.now() - started_time).total_seconds(),2),'s')

if __name__ == "__main__":
    eqn = input("Type your equation:\t")
    x = eval(input("Solve for x =\t"))
    time = datetime.now()
    var_eqn = eqn
    list_result = []
    cont = 'y'

    while 'NaN' not in list_result and cont.lower() == 'y' and x not in list_result:
        process = Solve(var_eqn, x)
        process.Solve()
        list_result.append(process.x)

        if process.x != 'NaN':
            print('x = \t', strfNumber(process.x))
            if len(list_result)==1:
                var_eqn = '(' + eqn.split("=")[0] + f')/(x-{list_result[0]})=0'
            else:
                div = f'(x-{list_result[0]})'
                for i in range(1, len(list_result)):
                    div += f'(x-{list_result[i]})'
                var_eqn = '(' + eqn.split("=")[0] + f')/({div})=0'

            cont = input('Try to find another solution? (Y/N):\t')
            if cont.lower() == 'y':
                x = eval(input("Solve for x =\t"))
            else:
                break
    show_result(eqn, list_result, time)
