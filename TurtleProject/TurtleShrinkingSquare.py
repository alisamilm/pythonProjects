import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green4")
drawing_board.title("Python Turtle")

#Yes, this time let's make interlocking squares

turtle_instance =turtle.Turtle()

def ss (size):
   for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

ss(150)
ss(130)
ss(110)
ss(90)
ss(70)
ss(50)
ss(30)
ss(10)

turtle.done()

#yes, that's how it's done