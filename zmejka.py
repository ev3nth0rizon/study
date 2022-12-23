import turtle
import time
import random

delay = 0.1

SCREEN_W = 600
SCREEN_H = 600
SCREEN_BORDER = 20

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(SCREEN_W, SCREEN_H)
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("blue")
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


def group():
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
		y = head.ycor()
		head.sety(y+20)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y-20)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x-20)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x+20)


wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []


while True:
	wn.update()
	# if head.xcor() >= SCREEN_H / 2 or head.xcor() <= -0.5 * SCREEN_H or head.ycor() >= SCREEN_W / 2 or head.ycor() <= -0.5 * SCREEN_W:
	if abs(head.xcor()) >= SCREEN_H / 2 or abs(head.ycor()) >= SCREEN_W / 2:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		colors = 'red'
		shapes = 'square'
		for segment in segments:
			segment.goto(SCREEN_H*10, SCREEN_W*10)
		segments.clear()
		delay = 0.1
		pen.clear()

	if head.distance(food) < 20:
		screen_h_border = SCREEN_H - SCREEN_BORDER * 2
		screen_w_border = SCREEN_W - SCREEN_BORDER * 2
		foodx = round((random.randint(0, screen_h_border) - (screen_h_border/2))/20, 0)
		x = 20 * foodx
		foody = round((random.randint(0, screen_w_border) - (screen_w_border/2))/20, 0)
		y = 20 * foody
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
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "Stop"
			colors = 'red'
			shapes = 'square'
			for segment in segments:
				segment.goto(SCREEN_H*10, SCREEN_W*10)
			segments.clear()
			delay = 0.1
			pen.clear()


	time.sleep(delay)