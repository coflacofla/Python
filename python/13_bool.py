#bool()

print(bool("python")) #데이터가 있으면 true, 없으면 false
print(bool("")) #false

print(bool([1,2,3])) #true

print(bool(4>5)) #false


a=2
print(bool(1<a<3)) #true, 조건을 양쪽으로 쓰는 bool이 가능,
#C에서는 and,or조건을 함께 써야 인식

print(bool(0)) #false

#if문/elif(else if아님주의)/else
#조건 문 뒤에 :로 끝남 주의 아두이노는 if{였음

#비교연산자

a = 10
b = 20

print(a!=b) #true


num = int(input("숫자를 입력하세요"))

result = num%2

if result == 0:
    print("짝수")
else :
    print("홀수")


