from func import formatNumber

class Polynomial():
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.result = []

    def Show(self):
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
