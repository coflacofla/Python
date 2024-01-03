import turtle as t



my_t = t.Turtle() #점수를 표시하는 용도(글씨쓰는용도)

my_t.penup()
my_t.goto(0,200)
my_t.pendown()
my_t.write("이채림의 집")
my_t.hideturtle()

#얘네는 그림 그리는 용도

t.speed(5)
t.hideturtle()

t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

#이동
t.pencolor("yellow")
t.penup()
t.pensize(10)
t.goto(0,100)
t.pendown()

t.color("cyan")
t.pensize(3)
t.fillcolor("yellow")
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()


