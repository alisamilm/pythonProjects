import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green4")
drawing_board.title("Python Turtle")

#let's draw a square

turtle_instance =turtle.Turtle()
'''
turtle_instance.forward(300)
turtle_instance.left(90)
turtle_instance.forward(300)
turtle_instance.left(90)
turtle_instance.forward(300)
turtle_instance.left(90)
turtle_instance.forward(300)
turtle_instance.left(90)
'''
#Yes, this is the hard way, we write the same thing four times, but let's loop it and write it only once.

for i in range(4):
    turtle_instance.forward(300)
    turtle_instance.left(90)

turtle.done()
