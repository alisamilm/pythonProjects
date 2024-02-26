import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green4")
drawing_board.title("Python Turtle")

#Let's draw a star quickly

turtle_instance = turtle.Turtle()

for i in range (5):
    turtle_instance.left(144)
    turtle_instance.forward(200)

turtle.done()

#Yes, this is how we made the star.