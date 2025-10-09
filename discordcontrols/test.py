def turtles_touching(turtle1, turtle2):
    import math
    a = (turtle1.xcor()-turtle2.xcor())
    b = (turtle1.ycor()-turtle2.ycor())
    c = math.sqrt(a**2 + b**2)
    return c < 30