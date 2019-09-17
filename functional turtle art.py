import turtle

turtle.shape("turtle")



def star():
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)


def square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
star()
turtle.penup()
turtle.forward(150)
turtle.pendown()
square()





turtle.exitonxlick()

