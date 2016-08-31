import turtle

def drawL():
    """
    To draw letter L
    :pre: (relative) pos(-125,0), right, pendown
    :post: (realtive) pos(-125,0), right, pendown
    return none
    """
    turtle.forward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(40)
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.pendown()

def drawI():
    """
    To draw letter I
    :pre: (relative) pos(-125,0), right, pendown
    :post: (realtive) pos(-125,0), right, pendown
    return none
    """
    turtle.forward(20)
    turtle.left(90)
    turtle.penup()
    turtle.forward(40)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(20)
    turtle.left(180)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(40)
    turtle.penup()
    turtle.left(90)
    turtle.forward(20)
    turtle.pendown()

def drawJ():
    """
    To draw letter J
    :pre: (relative) pos(-125,0), right, pendown
    :post: (realtive) pos(-125,0), right, pendown
    return none
    """
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(20)
    turtle.penup()
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()

def drawT():
    """
    To draw letter T
    :pre: (relative) pos(-125,0), right, pendown
    :post: (realtive) pos(-125,0), right, pendown
    return none
    """
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(20)
    turtle.penup()
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()

def drawH():
    """
    To draw letter H
    :pre: (relative) pos(-125,0), right, pendown
    :post: (realtive) pos(-125,0), right, pendown
    return none
    """
    turtle.left(90)
    turtle.forward(40)
    turtle.left(180)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(180)
    turtle.forward(40)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()

def drawA():
    """
    To draw letter A
    :pre: (relative) pos(-125,0), right, pendown
    :post: (realtive) pos(-125,0), right, pendown
    return none
    """
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()
    turtle.left(90)
    turtle.forward(10)
    turtle.pendown()

def main():
    """
    To draw a word
    :pre: home, right, pendown
    :post: relative pos(-125,0), right, pendown
    return none
    """
    turtle.penup()
    turtle.home()
    #starting the first letter towards left so that word comes in the center
    turtle.setposition(-125,0)
    turtle.pendown()
    turtle.color("blue")
    drawL()
    drawI()
    drawJ()
    drawI()
    drawT()
    drawH()
    drawA()
    turtle.mainloop()

if __name__=='__main__':
    main()
