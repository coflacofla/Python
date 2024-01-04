import turtle as t


while True:
    a = int(input("숫자 입력: "))

    if 3<=a<=9:
        for i in range(a):
            t.speed(5)
            t.pensize(3)
            t.pencolor("yellow")
            t.forward(100)
            t.left(360//a)
    
    else:
        print("3~9사이의 숫자로 다시 입력바랍니다.")
        
    

    
    
