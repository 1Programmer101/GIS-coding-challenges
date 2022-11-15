import turtle

n = int(input("How many sides does the polygon have"))

t = turtle.Turtle()

for x in range(n):
    t.forward(50)
    t.right(360/n)

turtle.done()
