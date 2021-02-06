from random import uniform
from datetime import datetime
from os import system
from functions import *

class Handle():
    def __init__(self, equation, x):
        self.equation = equation
        self.x = x
        self.list_sol = []

        self.ori_equa = equation

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
                    system('cls')
                    self.list_sol.append(self.x)
                    print(self.ori_equa)
                    print('x = \t', formatNumber(self.x))
                    print('L - R = ', strfNumber(round(Calc(self.equation, self.x),14)).replace('e+', ' x 10^').replace('e', ' x 10^'))
                    self.NEq()
                elif abs(Calc(self.equation, self.x)) < 10**-5 and abs(self.x) < 10**5:
                    print('x = \t', formatNumber(self.x))
                    print('L - R = ', strfNumber(Calc(self.equation, self.x)).replace('e+', ' x 10^').replace('e', ' x 10^'))
                    c = input('Continue? (Y/N):\t')
                    if c.lower() == 'y':
                        system('cls')
                        print(self.ori_equa)
                        times = 0
                    else:
                        break
                else:
                    system('cls')
                    print(self.ori_equa)
                    for i in self.list_sol:
                        print('x = \t', formatNumber(i))
                    print('Cannot Solve / The Equation Has No More Real Solution.')
        if Calc(self.equation, self.x) == 0:
            system('cls')
            self.list_sol.append(self.x)
            print(self.ori_equa)
            print('x = \t', formatNumber(self.x))
            print('L - R = ', strfNumber(Calc(self.equation, self.x)).replace('e+', ' x 10^').replace('e', ' x 10^'))
            self.NEq()

    def NEq(self):
        if len(self.list_sol)==0:
            print('Cannot Solve / The Equation Has No More Real Solution.')
        elif len(self.list_sol)==1:
            self.equation = f'({self.equation})/(x-{self.list_sol[0]})=0'
        else:
            div = f'(x-{self.list_sol[0]})'
            for i in range(1, len(self.list_sol)):
                div += f'*(x-{self.list_sol[i]})'
            self.equation = f'({self.equation})/({div})=0'
        c = input('Try to find another solution? (Y/N):\t')
        if c.lower() == 'y':
            self.x = eval(input("Solve for x =\t"))
            self.Solve()
        else:
            system('cls')
            print(self.ori_equa)
            for i in self.list_sol:
                print('x = \t', formatNumber(i))

if __name__ == "__main__":
    eqn = input("Type your equation:\t")
    x = eval(input("Solve for x =\t"))
    time = datetime.now()
    result = Handle(eqn, x).Solve()
    print('Solved in ',round((datetime.now() - time).total_seconds(),2),'s')
