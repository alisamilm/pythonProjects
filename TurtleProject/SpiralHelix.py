import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("black")
drawing_board.title("Python Turtle")

#Yes, now let's draw a circle.

'''
turtle_instance =turtle.Turtle()
turtle_instance.color("red")

turtle_instance.circle(100)

turtle.done()

#yes we can do it this way too
'''

color_list = ["red","blue","orange","purple","yellow"]
turtle.speed(0)
turtle_instance =turtle.Turtle()

for i in range(15):
    turtle_instance.color(color_list [i % 5])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)


turtle.done()

#Yes, we can draw colored circles on top of each other like this.
