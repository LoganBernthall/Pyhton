
#Exponents
x = 3 ** 3
print(x)

#Range function
for i in range(1, 11):
    print(i)

print("")

print(list(range(1,11)))


#Mini programming project:
import turtle
BACKGROUND_COLOUR = "#9EC388"
CRUST_COLOUR = "#ECA84F"
SAUCE_COLOUR = "#AD0509"
CHEESE_COLOUR = "#FBC70F"
PEPPERONI_LOCATIONS = [
    [-70,105],
    [-85,175],
    [-25,50],
    [-15,100],
    [-25,150],
    [-30,205],
    [15,50],
    [20,120],
    [20,200],
    [60,156],
    [71,215],
    [80,90],
    [95,150],
]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOUR)
screen.title("My Pizza")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")

def draw_circle(radius, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def move_turtle(x, y):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()

draw_circle(150, CRUST_COLOUR, CRUST_COLOUR)
move_turtle(0, 25)
draw_circle(125, SAUCE_COLOUR, CHEESE_COLOUR)

for location in PEPPERONI_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_circle(10, SAUCE_COLOUR, SAUCE_COLOUR)

move_turtle(0, 150)
my_turtle.color(BACKGROUND_COLOUR)

for x in range(0, 8):
    my_turtle.pendown()
    my_turtle.left(45)
    my_turtle.forward(150)
    my_turtle.penup()
    my_turtle.backward(150)

turtle.done()