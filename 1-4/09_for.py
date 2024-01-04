##for문##

#시퀀스를 순회하며 반복하는 구조. 시퀀수의 길이만큼 반복한다.
#for 제어변수 in 시퀀스 :
'''
for i in [1,2,3,4,5]:
    print(i)
    
for i in ('a','b','c',4,5):
    print(i)
for i in "python":
    print(i)
for i in range(100):
    print(i)
'''
#반복문을 써서 1-10까지의 합 구하기
'''
total = 0 #변수선언
for i in range(1,101):
    total +=i

print(total)


#중첩 반복문
for i in [1,2,3,4]:
    for j in['a','b']:
        print(i,j)
'''
#구구단 출력
#단을 입력 받아서 구구단을 출력해주세요

a = int(input("단:"))

for i in range(1,10):
    b = a*i
    print("{}X{} = {}".format(a,i,b))
    

