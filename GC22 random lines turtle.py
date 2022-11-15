import random
import turtle
t = turtle.Turtle()
while True:
    num = random.randint(1, 4)
    t.right(90*num)
    t.forward(100)
