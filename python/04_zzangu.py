import turtle

def draw_jjanggu_dad():
    # 창 크기 설정
    turtle.setup(width=800, height=600)

    # 몸 그리기
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()

    # 얼굴 그리기
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    # 눈 그리기
    turtle.penup()
    turtle.goto(-20, 0)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(20, 0)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

    # 입 그리기
    turtle.penup()
    turtle.goto(-20, -20)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(20, 180)

    # 손 그리기
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.color("blue")
    turtle.right(30)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)

    turtle.penup()
    turtle.goto(50, -50)
    turtle.pendown()
    turtle.color("blue")
    turtle.right(180)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)

    # 다리 그리기
    turtle.penup()
    turtle.goto(-30, -200)
    turtle.pendown()
    turtle.color("blue")
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(70)

    # 창 닫기
    turtle.done()

# 함수 호출하여 그리기
draw_jjanggu_dad()
