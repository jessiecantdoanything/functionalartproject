import turtle

scr = turtle.Screen()

turtle.shape("turtle")
kk = turtle.Turtle()
turtle.speed(.5)
turtle.color("Light Sea Green")


def star():
   for i in range(5):
       turtle.forward(150)
       turtle.right(144)


def square():
   for i in range(4):
       turtle.forward(100)
       turtle.right(90)



star()
turtle.begin_fill()
turtle.penup()
turtle.forward(250)
turtle.pendown()
turtle.end_fill()
square()




square()
turtle.penup()
turtle.right(90)
turtle.forward(150)
turtle.pendown()

turtle.right(30)
turtle.forward(40)


def pentagon():
    for i in range(4):
        turtle.forward(100)
        turtle.right(72)

def pentagon2():
    for i in range(25):
        pentagon()
        turtle.right(4)

pentagon2()
turtle.penup()
turtle.forward(350)
turtle.pendown()


turtle.forward(40)
turtle.right(30)
turtle.forward(150)
turtle.right(120)
turtle.forward(150)
turtle.right(120)
turtle.forward(150)





turtle.exitonclick()



