from turtle import  Turtle, Screen
timmy=Turtle()
timmy.shape("turtle")
timmy.color('yellow')
my_screen=Screen()
my_screen.bgcolor('green')
for steps in range(80):
    for c in ('blue', 'black', 'red'):
        timmy.color(c)
        timmy.forward(steps*steps)
        timmy.left(steps*3)
timmy.home()
print(my_screen.canvheight)
my_screen.exitonclick()





