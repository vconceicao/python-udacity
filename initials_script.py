import turtle

def draw_initials():

    window = turtle.Screen()
    

    abc =turtle.Turtle()
    abc.shape("arrow")
    abc.color("black")




    #for alphabet V
    abc.pu()
    abc.setpos(0,200)
    abc.pd()
    abc.seth(0)
    abc.right(75)
    abc.forward(200)
    abc.left(150)
    abc.forward(200)


    #for alphabet C
    abc.pu()
    abc.setpos(220,0)
    abc.pd()
    abc.seth(0)
    abc.backward(80)
    abc.right(90)
    abc.backward(200)
    abc.right(90)
    abc.backward(80)

  

    window.exitonclick()
    
draw_initials()
