import turtle
import time
import random

# Delay between moves
delay = 0.1

# Score variables
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0, 100)

# Snake body segments
segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

# Main game loop
while True:
    wn.update()

    # Check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the body segments
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        # Reset score
        score = 0
        delay = 0.1

        # Update the scoreboard
        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check for collision with food
    if head.distance(food) < 20:
        # Move food to a new location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Reduce delay slightly (increase speed)
        delay = max(0.05, delay - 0.002)

        # Increase score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the segments in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move first segment to where the head is
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for collision with self
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            # Reset score
            score = 0
            delay = 0.1

            # Update scoreboard
            pen.clear()
            pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
