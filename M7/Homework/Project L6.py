import turtle 

# Create screen
sc = turtle.Screen()
sc.bgcolor("pink")
sc.setup(500, 500)
turtle.title("Welcome to Turtle Window")

# Create turtle
board = turtle.Turtle()
board.color("blue")          # Outline color
board.fillcolor("yellow")    # Fill color

# Begin filling
board.begin_fill()

n = 8  # Number of sides
for i in range(n):
    board.forward(100)
    board.left(360 / n)

# End filling
board.end_fill()
turtle.done()
# This code creates a turtle graphics window and draws a filled octagon with specified colors.