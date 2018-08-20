import turtle;




def draw_square(some_turtle):

    turtle = some_turtle
    
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)

     


def draw_art():

    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    draw_square(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    triangle = turtle.Turtle()
    triangle.color("green")
    triangle.forward(100)
    triangle.left(120)
    triangle.forward(100)
    triangle.left(120)
    triangle.forward(100)

    
    window.exitonclick()
    
draw_art()          
