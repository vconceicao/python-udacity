import turtle

def circle_squares():


    window = turtle.Screen()
    window.bgcolor("green")
    
    brad = turtle.Turtle()
    


    for j in range(24):    
        for i in  range(4):
            brad.forward(100)
            brad.right(90)
        brad.right(15)

    window.exitonclick() 

circle_squares()
