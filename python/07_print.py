# 변수선언
name = "이채림"
days = 6
course = "파이썬"
#변수설정 규칙
#401_name선언 시 invalid error발생. 숫자로 시작할 수 없음
#if_name이라고 하면 ok
#_name도ok
#!name 은 안됨 특수기호는 안됨 유일하게 가능한 게 _언더바. 



#변수 type 확인 가능, C보다 큰 data메모리. 파이썬은 실행하며 자료형 type이 결정됨.

print(type(name))
print(type(days))
print('------')
#data가 갖는 주소 정보 출력
print(id(name)) 
print(id(days))


print(1,2,3)
print('a','b','c')


print('---- print("a","b",c")-----')
#문자열 안에 또 큰따옴표가 있어서 syntax error발생 이럴 때는 밖에거를 작은 따옴표로
print("파이썬 시작합니다. 저는 이채림입니다. 6일동안 화이팅")

print('---- print(a+b+c)-----')
print("""파이썬 시작합니다.
저는 이채림입니다.
6일동안 화이팅.""")

print("""파이썬 시작합니다.\n 저는 이채림입니다. \n6일동안 화이팅""")
print('-----')
print(course,"시작합니다.\n 저는 ",name,"입니다.\n ",days,"일 동안 화이팅")
print('-----')

print(course+"시작합니다.\n 저는 "+name+"입니다.\n "+str(days)+"일 동안 화이팅")
#얘는 error왜냐하면 days는 숫자라서. ++는 문자형 data만 더해서 쓸 수 있음
#이럴 때는 형변환 필요 str 써서

print('----f스트링----')
print(f"""{course}시작합니다.
저는 {name} 입니다.
{days}일 동안 화이팅""")


print(1+2) #끝문장 enter됨
print(1,2,3,4,5,6, end =':', sep='-')  #끝문장 enter안됨 data 연달아서 쓸 수 있음 
print("new line test")


print(f"""{course}시작합니다.
즐거운 시간.
저는 {name}입니다.
{days}일 동안 {course}진행합니다.
""")
