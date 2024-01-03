from turtle import*

screen = Screen() #객체선언
t = Turtle()
screen.title("My page") 
#size=1


def forward_move(): #함수 정의
    t.forward(10)
def backward_move():
    t.backward(10)
def left_move():
    t.left(10)
def right_move():
    t.right(10)
def clear_all():
    t.up()
    t.clear()
    t.home()
    t.down()
def pensize_plus():
    t.pensize(t.pensize() +1)
def pensize_minus():
    t.pensize(t.pensize() -1)
def pen_updown():
    if t.isdown() == False:
     t.pendown()
    else:
     t.penup()


def undo():
    t.undo()


    
#def pensize_plus():
#   global size
#   size = size +1
#    t.pensize(size)

#def pensize_minus():
#    global size
#    if size > 1:
#        size = size -1
#        t.pensize(size)

screen.listen()
screen.onkeypress(forward_move,'Up') #up키,down키 약속된 키워드:대소문자 맞춰주기
screen.onkeypress(backward_move,'Down')

#왼쪽 화살표 왼쪽으로 턴
#오른쪼기 화살표 오른쪽으로 턴

screen.onkeypress(left_move, 'Left')
screen.onkeypress(right_move,'Right')

#c키를 누르면 화면 클리어, 초기 위치로 이동

screen.onkeypress(clear_all, 'c')

#펜 사이즈를 +와 -를 누르면 조절될 수 있도록

screen.onkeypress(pensize_plus, '+')
screen.onkeypress(pensize_minus, '-')

#pen up/ down

screen.onkeypress(pen_updown, 'Return')

#undo/ctrl+z 기능

screen.onkeypress(undo, 'u')







