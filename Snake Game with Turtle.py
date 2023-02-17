from turtle import *
from time import sleep
from random import *

#Functions
def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    if head.direction == 'left':
        head.setx(head.xcor() - 20)
    if head.direction == 'down':
        head.sety(head.ycor() - 20)
    if head.direction == 'right':
        head.setx(head.xcor() + 20)

def up():
    if head.direction != 'down':
        head.direction = 'up'
def left():
    if head.direction != 'right':
        head.direction = 'left'
def right():
    if head.direction != 'left':
        head.direction = 'right'
def down():
    if head.direction != 'up':
        head.direction = 'down'

#Variables
turtle_size = 1
delay = 0.1
turtle_dist = 20
Width = 600
Height = 600
segments = []
score = 0
high_score = 0

#Setup Screen
wn = Screen()
wn.title('Snake Game')
wn.bgcolor('#000000')
wn.setup(width = Width, height = Height)
wn.tracer(0)

# Snake Head
head = Turtle()
head.speed(0)
head.shape('square')
head.shapesize(turtle_size, turtle_size, 1)
head.color('#00ff00')
head.penup()
head.direction = 'stop'

#Snake Food
food = Turtle()
food.speed(0)
food.shape('circle')
food.shapesize(turtle_size, turtle_size, 1)
food.color('#ff7100')
food.penup()
head.direction = 'stop'
x = randint((turtle_dist - Width)/2, (Width - turtle_dist)/2)
y = randint((turtle_dist - Height)/2, (Height - turtle_dist)/2)
food.goto(x-10, y-10)

#Pen
pen = Turtle()
pen.speed(0)
pen.shape('square')
pen.color('#aaaa00')
pen.penup()
pen.hideturtle()
pen.goto(0, (Width-80)/2)
pen.write('Score: 0     Highscore: 0', align='center', font=('Courier', 20, 'normal'))

#Keyboard Bindings   
wn.listen()
wn.onkeypress(up, 'Up')
wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')
wn.onkeypress(down, 'Down')

# Main Game Loop
while True:
    wn.update()
    # Check for food collision
    if head.distance(food) < turtle_dist:
        x = int(randint((turtle_dist - Width) / 2, (Width - turtle_dist) / 2)/20)*20
        y = int(randint((turtle_dist - Height) / 2, (Height - turtle_dist) / 2)/20)*20
        food.goto(x, y)
        delay -= 0.001
        # Add a new segment
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('#aaff00')
        new_segment.penup()
        segments.append(new_segment)
        # Increase the score
        score += 6
        if score > high_score:
            high_score = score
    pen.clear()
    pen.write('Score: {}     Highscore: {}'.format(score, high_score), align='center', font=('Courier', 20, 'normal'))
    #Check for border collision
    if head.xcor() > (Width - turtle_dist)/2 or head.xcor() < (turtle_dist - Width)/2 or head.ycor() > (Height - turtle_dist)/2 or head.ycor() < (turtle_dist - Height)/2:
        sleep(1)
        score = 0
        delay = 0.1
        head.goto(0, 0)
        head.direction = 'stop'
        #Hide the body
        for segment in segments:
            segment.goto(Width*2, Height*2)
        #Clear the list of segments
        segments.clear()
    # Check for body collision
    for segment in segments:
        if segment.distance(head) < 20:
            sleep(1)
            score = 0
            delay = 0.1
            head.goto(0, 0)
            head.direction = 'stop'
            # Hide the body
            for segment in segments:
                segment.goto(Width * 2, Height * 2)
            # Clear the list of segments
            segments.clear()
    #Move segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    #Move the final segment closest to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    sleep(delay)

wn.mainloop()









