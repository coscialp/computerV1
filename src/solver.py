from lib2to3.pgen2.literals import simple_escapes
import re
from math import Math

class Solver:
    def __init__(self, arg) -> None:
        self.parse(arg)

    def __repr__(self) -> str:
        return f'equation: {self.left} = {self.right}\na: {self.a} b: {self.b} c: {self.c}\nra: {self.ra} rb: {self.rb} rc: {self.rc}'

    def parse(self, arg) -> None:
        self.left = arg.split('=')[0].replace(' * ', '').replace(' / ', '/').replace('X^0', '').replace('X^1', 'X').replace('- ', '-').replace('+ ', '').split(' ')
        self.right = arg.split('=')[-1].replace(' * ', '').replace('X^0', '').replace('X^1', 'X').replace('- ', '-').replace('+ ', '').split(' ')
        self.delta = None
        # self.simplification_base()
        self.parse_left()
        self.parse_right()
        self.simplifiy()
        print(self.get_descrimant())
        
    # def simplification_base(self) -> None:
    #     for i in range(len(self.left)):
    #         print(self.left[i])
    #         if self.left[i].count("X") > 1:
    #             print(self.left[i].split('*'))
    #             number = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", self.left[i])
    #             tmp = 1
    #             for n in number:
    #                 tmp *= float(n)
    #             self.left[i] = f'{tmp} * X^2'
    #         elif self.left[i].count("X") == 0 and self.left[i].count('*'):
    #             number = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", self.left[i])
    #             tmp = 1
    #             for n in number:
    #                 tmp *= float(n)
    #             self.left[i] = f'{tmp}'
    #         elif self.left[i].count("X") == 0 and self.left[i].count('/'):
    #             number = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", self.left[i])
    #             tmp = 1
    #             for n in number:
    #                 tmp = float(n) / tmp if tmp == 1 else tmp / float(n)
    #             self.left[i] = f'{tmp}'

    def simplifiy(self):
        self.a -= self.ra
        self.b -= self.rb
        self.c -= self.rc
        ra, rb, rc = 0, 0, 0

    def get_descrimant(self):
        if not self.delta:
            self.delta = self.b**2 - 4 * self.a * self.c
        return self.delta

    def parse_left(self) -> None:
        self.a, self.b, self.c = 0, 0, 0
        a, b, c = [], [], []
        for tok in self.left:
            if tok.find("X^2") != -1:
                a.append(float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", tok)[0]))
            elif tok.find("X") != -1:
                b.append(float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", tok)[0]))
            elif tok:
                c.append(float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", tok)[0]))
        
        for n in a:
            self.a += n
        for n in b:
            self.b += n
        for n in c:
            self.c += n

        self.a = round(self.a, Math.get_precision(self.a)) if Math.get_precision(self.a) != 0 else int(self.a)
        self.b = round(self.b, Math.get_precision(self.b)) if Math.get_precision(self.b) != 0 else int(self.b)
        self.c = round(self.c, Math.get_precision(self.c)) if Math.get_precision(self.c) != 0 else int(self.c)

    def parse_right(self) -> None:
        self.ra, self.rb, self.rc = 0, 0, 0
        ra, rb, rc = [], [], []
        for tok in self.right:
            if tok.find("X^2") != -1:
                ra.append(float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", tok)[0]))
            elif tok.find("X") != -1:
                rb.append(float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", tok)[0]))
            elif tok:
                rc.append(float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", tok)[0]))
        
        for n in ra:
            self.ra += n
        for n in rb:
            self.rb += n
        for n in rc:
            self.rc += n

        self.ra = round(self.a, Math.get_precision(self.ra)) if Math.get_precision(self.ra) != 0 else int(self.ra)
        self.rb = round(self.b, Math.get_precision(self.rb)) if Math.get_precision(self.rb) != 0 else int(self.rb)
        self.rc = round(self.c, Math.get_precision(self.rc)) if Math.get_precision(self.rc) != 0 else int(self.rc)
