import turtle
import time
import random

delay = 0.1

SCREEN_W = 600
SCREEN_H = 600
SCREEN_BORDER = 20

scr = turtle.Screen()
scr.bgcolor('black')
scr.setup(SCREEN_W, SCREEN_H)
scr.tracer(0)

head = turtle.Turtle()
head.shape('circle')
head.color('blue')
head.penup()
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
colors = 'red'
shapes = 'square'
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)


def goup():
	if head.direction != "down":
		head.direction = "up"


def godown():
	if head.direction != "up":
		head.direction = "down"


def goleft():
	if head.direction != "right":
		head.direction = "left"


def goright():
	if head.direction != "left":
		head.direction = "right"


def move():
	if head.direction == "up":
		movey = head.ycor()
		head.sety(movey+20)
	if head.direction == "down":
		movey = head.ycor()
		head.sety(movey-20)
	if head.direction == "left":
		movex = head.xcor()
		head.setx(movex-20)
	if head.direction == "right":
		movex = head.xcor()
		head.setx(movex+20)


scr.listen()
scr.onkeypress(goup, "w")
scr.onkeypress(godown, "s")
scr.onkeypress(goleft, "a")
scr.onkeypress(goright, "d")

segments = []


def genxy():
	screen_h_border = SCREEN_H - SCREEN_BORDER * 2
	screen_w_border = SCREEN_W - SCREEN_BORDER * 2
	foodx = round((random.randint(0, screen_h_border) - (screen_h_border / 2)) / 20, 0)
	x1 = 20 * foodx
	foody = round((random.randint(0, screen_w_border) - (screen_w_border / 2)) / 20, 0)
	y1 = 20 * foody
	return x1, y1


while True:
	scr.update()
	if abs(head.xcor()) >= SCREEN_H / 2 or abs(head.ycor()) >= SCREEN_W / 2:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		colors = 'red'
		shapes = 'square'
		for segment_loop1 in segments:
			segment_loop1.goto(SCREEN_H * 10, SCREEN_W * 10)
		segments.clear()
		delay = 0.1
		pen.clear()
		food.goto(0, 100)

	if head.distance(food) < 20:
		while True:
			x, y = genxy()
			break_snake = False
			for segment in segments:
				if x == segment.xcor() and y == segment.ycor():
					break_snake = True
					break
			if not break_snake:
				break
		food.goto(x, y)

		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("green")
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001
		pen.clear()

	for index in range(len(segments)-1, 0, -1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)
	move()
	for segment_loop1 in segments:
		if segment_loop1.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "Stop"
			colors = 'red'
			shapes = 'square'
			for segment_loop2 in segments:
				segment_loop2.goto(SCREEN_H * 10, SCREEN_W * 10)
			segments.clear()
			delay = 0.1
			pen.clear()
			food.goto(0, 100)

	time.sleep(delay)
