from functools import reduce
import re
from math import Math

class Solver:
    def __init__(self, arg) -> None:
        self.parse(arg)
        self.resolver()

    def __repr__(self) -> str:
        return f'equation: {self.left} = {self.right}\na: {self.a} b: {self.b} c: {self.c}\nra: {self.ra} rb: {self.rb} rc: {self.rc}'

    exposant = {
        '0': '⁰',
        '1': '¹',
        '2': '²',
        '3': '³',
        '4': '⁴',
        '5': '⁵',
        '6': '⁶',
        '7': '⁷',
        '8': '⁸',
        '9': '⁹',
        '-': '⁻'
        }

    def parse(self, arg) -> None:
        self.left = arg.split('=')[0].replace(' * ', '').replace('x', 'X').replace(' / ', '/').replace('X^0', '').replace('X^1', 'X').replace('- ', '-').replace('+ ', '').split(' ')
        self.right = arg.split('=')[-1].replace(' * ', '').replace('x', 'X').replace('X^0', '').replace('X^1', 'X').replace('- ', '-').replace('+ ', '').split(' ')
        self.equation = arg.replace('x', 'X').replace('X ', 'X^1').replace(' ', '')

        print(f'Equation: {Solver.get_equation(arg)}')
        
        self.get_degree()

        # self.parsing()
        # self.left = arg.split('=')[0]
        # self.right = arg.split('=')[-1]
        self.delta = None
        self.parse_left()
        self.parse_right()
        self.simplifiy()
        if (self.degree <= 2):
            self.reduced_form()
        
    def get_equation(arg) -> str:
        arg = arg.replace(' * ', '').replace('x', 'X')
        message = ''
        count = 0
        for idx in range(len(arg)):
            if arg[idx] == '^':
                count += 1
                continue
            message += Solver.exposant.get(arg[idx]) if Solver.exposant.get(arg[idx]) and idx > 0 + count and message[idx - 1 - count] in 'X⁻⁰¹²³⁴⁵⁶⁷⁸⁹' else arg[idx]
        return message

    def reduced_form(self) -> None:
        reduced = 'Reduced form:'
        if self.a:
            reduced += f' {self.a}X^2 '
        if self.b:
            reduced += f'{"+" if self.b > 0 and self.a != 0 else ""} {self.b}X '
        if (self.c):
            reduced += f'{"+" if self.c > 0 and self.b != 0 and self.a != 0 else ""}{self.c} '
        reduced += '= 0'
        reduced = reduced.replace(' -', ' - ')
        print(Solver.get_equation(reduced))

    def resolver(self) -> None:
        if self.degree == 2:
            self.get_descrimant()
            self.calculator()
        elif self.degree == 1:
            print(f'The solution are:\nx₀ = {-self.c / self.b}')
        elif self.degree == 0:
            if self.c == self.rc:
                print(f'The solution are: X ∈ ℝ')
            else:
                print('The equation has no solution!')
        else:
            print('The polynomial degree is stricly greater than 2, I can\'t solve.')

    # def parsing(self) -> None:
    #     self.parsed = []
    #     print(f'{self.equation}')
    #     jdx = 0
    #     for idx in range(len(self.equation)):
    #         if self.equation[idx] in "*-+/=":
    #             self.parsed.append(self.equation[jdx:idx])
    #             self.parsed.append(self.equation[idx])
    #             jdx = idx + 1
    #     self.parsed.append(self.equation[jdx:])
    #     for idx in range(len(self.parsed)):
    #         if self.parsed[idx] == '-':
    #             self.parsed[idx] = '+'
    #             self.parsed[idx + 1] = f'-{self.parsed[idx + 1]}'
    #     print(self.parsed)

    # def simplification(self) -> None:
    #     for idx in range(len(self.parsed)):
    #         if self.equation[idx] == "*":
    #             if self.equation[idx + 1].count('X^2') and self.equation[idx - 1].count('X'):

    def get_degree(self) -> None:
        self.degree = 0
        i = 0
        if (self.equation[-1] == '^'):
            print('Error: Coefficient are not valid!')
            exit(1)
        while i < len(self.equation):
            if self.equation[i] == '^':
                if (not self.equation[i - 1] == 'X'):
                    print('Error: Coefficient are not valid!')
                    exit(1)
                j = i + 1
                degree_tmp = 0
                while j in range(len(self.equation)):
                    if self.equation[j - 1] == '^' and (self.equation[j] in '-*/+='):
                        print('Error: Coefficient are not valid!')
                        exit(1)
                    if self.equation[j] in '.':
                        print('Error: Coefficient are not valid!')
                        exit(1)
                    if not self.equation[j].isdigit():
                        break
                    degree_tmp = degree_tmp * 10 + int(self.equation[j])
                    j += 1
                if degree_tmp > self.degree:
                    self.degree = degree_tmp
            i += 1
        print(f'Polynomial degree: {self.degree}')
    



    def simplifiy(self):
        if (self.degree != 0):
            self.a -= self.ra
            self.b -= self.rb
            self.c -= self.rc
            ra, rb, rc = 0, 0, 0

    def get_descrimant(self):
        if not self.delta:
            self.delta = self.b**2 - 4 * self.a * self.c
        print(f'Δ = {self.delta}')

    def calculator(self):
        if self.delta < 0:
            print('Discriminant is strictly negative, the equation has no solution!')
        elif self.delta == 0:
            print(f'Discriminant is equal to zero, the once solution are:\nx₀ = {-self.b / (2 * self.a)}')
        else:
            print(f'Discriminant is strictly positive, the two solutions are:\nx₁ = {(-self.b - Math.sqrt(self.delta)) / (2 * self.a)}\nx₂ = {(-self.b + Math.sqrt(self.delta)) / (2 * self.a)}')

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
