import turtle

# 오른쪽 위에 하늘색 구름 그리기
turtle.penup()
turtle.goto(200, 200)
turtle.pendown()
turtle.color("skyblue")
turtle.begin_fill()

for _ in range(3):
    turtle.circle(30, 180)
    turtle.left(180)
turtle.end_fill()

# 왼쪽 아래에 간단한 집 모양 그리기
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
