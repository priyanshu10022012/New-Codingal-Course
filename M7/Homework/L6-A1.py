import turtle 
sc = turtle.Screen()
sc.bgcolor("pink")
sc.setup(500, 500)
turtle.title("Welcome to Turtle Window")
board = turtle.Turtle()
n = 8
for i in range(n):
    board.forward(100)
    board.left(360/n)
turtle.done()
# This code creates a turtle graphics window and draws an octagon.