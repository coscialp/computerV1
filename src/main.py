import sys
from solver import Solver
from math import Math


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Error: Wrong number of arguments')
        exit(1)
    solver = Solver(sys.argv[-1])
    # print(solver)