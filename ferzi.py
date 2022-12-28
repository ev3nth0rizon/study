import turtle
import time

SCREEN_W = 800
SCREEN_H = 800

chessboard = turtle.Turtle()
chessboard.screen.tracer(0, 0)

scr = turtle.Screen()
scr.setup(SCREEN_H, SCREEN_W)

tstar = turtle.Turtle()
tstar.screen.tracer(0, 0)
tstar.color('red')
tstar.penup()


def star(x, y):
    tstar.goto(-425 + (x * 100), 460 - (y * 100))
    tstar.pendown()
    tstar.begin_fill()
    for z in range(5):
        tstar.right(144)
        tstar.forward(50)
    tstar.end_fill()
    tstar.penup()


def smallsquare():
    chessboard.begin_fill()
    for m in range(4):
        chessboard.forward(100)
        chessboard.right(90)
    chessboard.end_fill()


def bigsquare():
    for i in range(8):
        for j in range(8):
            chessboard.penup()
            chessboard.goto(-400 + (j * 100), 400 - (i * 100))
            chessboard.pendown()
            k = i + j
            if k / 2 == k // 2:
                chessboard.fillcolor('white')
            else:
                chessboard.fillcolor('black')
            smallsquare()


def under_attack(column, existing_queens):
    row = len(existing_queens)+1
    for queen in existing_queens:
        r, c = queen
        if r == row:
            return True
        if c == column:
            return True
        if (column-c) == (row-r):
            return True
        if (column-c) == -(row-r):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]
    smaller_solutions = solve(n-1)
    solutions = []
    for solution in smaller_solutions:
        for column in range(1, 9):
            if not under_attack(column, solution):
                solutions.append(solution + [(n, column)])
    if n == 8:
        for y in range(20):
            for p in solutions[y]:
                (x, y) = p
                star(x, y)
                chessboard.screen.update()
            time.sleep(5)
            tstar.screen.update()
            bigsquare()
    return solutions


bigsquare()
solve(8)
