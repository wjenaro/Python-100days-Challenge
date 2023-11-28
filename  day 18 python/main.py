from turtle import Turtle, Screen

# Function to draw a rectangle
def draw_rectangle(turtle, width, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(width if _ % 2 == 0 else height)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a triangle
def draw_triangle(turtle, size, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

# Set up the turtle
timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.speed(2)  # Set turtle speed

# Draw the house
draw_rectangle(timmy_the_turtle, 200, 150, 'yellow')  # House

# Draw the triangular roof
timmy_the_turtle.penup()
timmy_the_turtle.goto(-100, 75)
timmy_the_turtle.pendown()
draw_triangle(timmy_the_turtle, 200, 'red')  # Roof

# Draw the door
timmy_the_turtle.penup()
timmy_the_turtle.goto(50, -75)
timmy_the_turtle.pendown()
draw_rectangle(timmy_the_turtle, 50, 75, 'brown')  # Door

# Draw the windows
for window_position in [(20, 0), (90, 0)]:
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(window_position)
    timmy_the_turtle.pendown()
    draw_rectangle(timmy_the_turtle, 40, 75, 'cyan')  # Windows

# Close the window on click
screen = Screen()
screen.exitonclick()
