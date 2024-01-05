#class 생성

class Human:
    def __init__(self,name,age,sex): #self 생성자 
        self.name = name
        self.age = age
        self.sex = sex
    def play(self): #클래스 객체 선언
        print("노는 중")


wife = Human("안나",25,"여자")
print(wife.name)
print(wife.age)
print(wife.sex)

print()
son = Human("손많이가",6,"남자")
print(son.name)
print(son.age)
print(son.sex)

son.play()
