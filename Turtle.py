import turtle

""" turtle.shape("turtle")
for i in range(0, 5):   
    turtle.forward(100)    
    turtle.right(72)
turtle.exitonClick() """


""" for i in range(0, 10):   
    turtle.right(36)    
    for i in range(0, 5):        
        turtle.forward(100)        
        turtle.right(72)
turtle.exitonClick() """


""" turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 4):    
    turtle.forward(70)    
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0, 4):    
    turtle.forward(70)    
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)
turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
for i in range(0, 4):    
    turtle.forward(70)    
    turtle.right(90)
turtle.end_fill()
turtle.exitonClick()
 """

""" import random
for x in range(0,10):    
    for i in range(0,8):        
        turtle.forward(50)        
        turtle.right(45)    
        turtle.right(36)
turtle.hideturtle()
turtle.exitonClick() """


import random
lines = random.randint(5, 20)
for x in range(0,lines):    
    length = random.randint(25, 100)    
    rotate = random.randint(1, 365)    
    turtle.forward(length)    
    turtle.right(rotate)
turtle.exitonClick()