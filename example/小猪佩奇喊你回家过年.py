#小猪佩奇喊你回家过年  ---By Miezatone
#Pythone 手绘

import turtle
turtle.pensize(3)

turtle.penup()          #三角形
turtle.goto(-200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.circle(40,steps=3)
turtle.end_fill()

turtle.penup()          #四边形
turtle.goto(-100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
turtle.circle(40,steps=4)
turtle.end_fill()

turtle.penup()           #五边形
turtle.goto(0,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('green')
turtle.circle(40,steps=5)
turtle.end_fill()

turtle.penup()           #六边形
turtle.goto(100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow')
turtle.circle(40,steps=6)
turtle.end_fill()


turtle.penup()           #圆形
turtle.goto(200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('purple')
turtle.circle(40)
turtle.down()
turtle.end_fill()

turtle.color('green')         #表示文字颜色
turtle.penup()
turtle.goto(-130,50)
turtle.pendown()
turtle.write(("小猪佩奇喊你回家过年"),font=("华文楷体",28,"bold"))
turtle.hideturtle()
turtle.done()
