import turtle
import time

SCREEN_W = 800
SCREEN_H = 800

chessboard = turtle.Turtle()
chessboard.screen.tracer(0, 0)

scr = turtle.Screen()
scr.bgcolor('black')
scr.setup(SCREEN_H, SCREEN_W)
scr.tracer(0)

queen = turtle.Turtle()



def star(coord_list):
    for i in range(8):
        x = coord_list[i].xcor * 100 - 50
        y = coord_list[i].ycor * 100 - 50
        queen.goto(x, y)
        queen.pendown()
        for i in range(5):
            queen.forward(60)
            queen.right(144)
        queen.fillcolor('red')
        queen.penup()


for i in range(4):
    chessboard.forward(800)
    chessboard.right(90)

def perebor_doski():
    doska = []
    for i in range(8):
        for j in range(8):
            doska.append((i, j))
    return doska


def hit_by(coords1, coords2):
    if coords1[0] == coords2[0] or coords1[1] == coords2[1] or abs(coords1[0] - coords2[0]) == abs(coords1[1] - coords2[1]):
        return True
    else:
        return False



def smallsquare():
    chessboard.begin_fill()
    for m in range(4):
        chessboard.forward(100)
        chessboard.right(90)
    chessboard.end_fill()


scr.listen()
# scr.onkeypress(shuffle, "w")

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
chessboard.screen.update()
time.sleep(100)

queens = []
queens.append((1,1))

for k in range(7):
    for i in range(8):
       for j in range(8):
           m = (i,j)
        if not hit_by(queens[i],m):
            queens.append(l)
            break



