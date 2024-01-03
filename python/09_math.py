#연산 +,-,*,/,%,//

a = 14
b = 7
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #나머지
print(a//b) #몫

x = -1
y = 3

print(-(y*y*y)+2*(x*x*y))


#문자열 연산
a = "파이썬"
b = "파이팅"

print(a+b)

print(a*4) #가능,+랑 *숫자만 가능

print(len(a)) #문자열 길이


#문자열 인덱싱 슬라이싱
print(a[2]) #썬 [인덱싱]

a = "Life is too short, you need python"
b = "나는 올해 30살 입니다"

print(a[2]) #f
#a[시작 인덱스:끝 인덱스-1:간격]
print(a[28:]) #python

print(b[6:9]) #30살


#"짝"만 출력하기
c = "홀짝홀짝홀짝홀짝"

print(c[1::2]) #짝짝짝짝


#문자열을 뒤집어서 출력
d = " PYTHON PYTHON "

print(d[::-1]) #음의 인덱스 사용

print(d.count('O')) #O의 개수를 count
print(",".join(d)) #join을 써서 문자열 하나하나 사이에 ,를 삽입
print("+".join(d))
print(d.lower()) #소문자로 바꾸기

print(d.lstrip())
print(d.rstrip())

#P값을 A로 바꾸기
#d[2] = 'p' 이렇게 문자열의 수정은 불가능함  



