import turtle

def draw_flowers():

    window = turtle.Screen()

    brad = turtle.Turtle()


    for i in range(36):        
        for i in range(4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    brad.right(90)    
    brad.forward(350)
        
        
    window.exitonclick()

draw_flowers()
