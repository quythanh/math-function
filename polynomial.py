from functions import formatNumber, abs
from math import acos, cos

class Polynomial():
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.result = []
        self.pi = 3.141592653589793

    def Show(self):
        print('─'*50)
        if len(self.result) == 1:
            print(f"x = {self.result[0]}")
        else:
            for i in range(len(self.result)):
                print(f"x{i+1} = {self.result[i]}")

    def Degree_1(self):
        x = str(formatNumber(round(-self.b/self.a, 15)))
        self.result.append(x)
        self.Show()

    def Degree_2(self):
        delta = self.b**2 - 4*self.a*self.c
        if delta == 0:
            x = str(formatNumber(round(-self.b/(2*self.a)), 15))
            self.result.append(x)
        elif delta > 0:
            x1 = str(formatNumber(round((-self.b+(delta)**(1/2))/(2*self.a), 15)))
            x2 = str(formatNumber(round((-self.b-(delta)**(1/2))/(2*self.a), 15)))
            self.result.append(x1)
            self.result.append(x2)
        else:
            real = str(formatNumber(round(-self.b/(2*self.a), 15)))
            imagine = str(formatNumber(round((-delta)**(1/2)/(2*a), 15)))
            x1 = real + " + " + imagine + "i"
            x2 = real + " - " + imagine + "i"
            self.result.append(x1)
            self.result.append(x2)
        self.Show()

    def Degree_3(self):
        delta = self.b**2 - 3*self.a*self.c
        k = (9*self.a*self.b*self.c-2*self.b**3-27*self.a**2*self.d)/(2*(abs(delta**3))**0.5)
        if delta > 0:
            if abs(k) < 1:
                x1 = str(formatNumber(round((2*delta**0.5*cos(acos(k)/3)-self.b)/(3*self.a), 15)))
                x2 = str(formatNumber(round((2*delta**0.5*cos((acos(k)-2*self.pi)/3)-self.b)/(3*self.a), 15)))
                x3 = str(formatNumber(round((2*delta**0.5*cos((acos(k)+2*self.pi)/3)-self.b)/(3*self.a), 15)))
                self.result.append(x1)
                self.result.append(x2)
                self.result.append(x3)
            elif abs(k) == 1:
                x1 = str(formatNumber(round((2*delta**0.5-self.b)/(3*self.a), 15)))
                x2 = str(formatNumber(round((-delta**0.5-self.b)/(3*self.a), 15)))
                self.result.append(x1)
                self.result.append(x2)
            else:
                x = str(formatNumber(round((delta**0.5*abs(k)/(3*self.a*k))*((abs(k)+(k*k-1)**0.5)**(1/3)+(abs(k)-(k*k-1)**0.5)**(1/3))-self.b/(3*self.a), 15)))
                self.result.append(x)
        elif delta == 0:
            x = str(formatNumber(round((-self.b+(self.b**3-27*self.a**2*self.d)**(1/3))/(3*self.a), 15)))
            self.result.append(x)
        else:
            x = str(formatNumber(round((abs(delta)**0.5/(3*self.a))*((k+(k*k+1)**0.5)**(1/3)-((k*k+1)**0.5-k)**(1/3))-self.b/(3*self.a), 15)))
            self.result.append(x)
        self.Show()

if __name__ == "__main__":
    a, b, c, d, e = 0, 0, 0, 0, 0
    dg = input("Degree? (1-4):\t")

    if dg == "1":
        print("ax + b = 0")
        a = eval(input("a = "))
        b = eval(input("b = "))
        Polynomial(a, b, c, d, e).Degree_1()
    elif dg == "2":
        print("ax^2 + bx + c = 0")
        a = eval(input("a = "))
        b = eval(input("b = "))
        c = eval(input("c = "))
        Polynomial(a, b, c, d, e).Degree_2()
    elif dg == "3":
        print("ax^3 + bx^2 + cx + d = 0")
        a = eval(input("a = "))
        b = eval(input("b = "))
        c = eval(input("c = "))
        d = eval(input("d = "))
        Polynomial(a, b, c, d, e).Degree_3()
    elif dg == "4":
        print("ax^4 + bx^3 + cx^2 + dx + e = 0")
        a = eval(input("a = "))
        b = eval(input("b = "))
        c = eval(input("c = "))
        d = eval(input("d = "))
        e = eval(input("e = "))
        Polynomial(a, b, c, d, e).Degree_4()
