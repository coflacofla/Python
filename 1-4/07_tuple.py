###tuple

t = ()
t1 = ('dlcofla',1,)
t2 = (1,2,3,'b')

print(t1)

print(t2[0])

#+연산

print(t1+t2)

#길이 추출 len 함수
print(len(t2))
print(len(t1))
print(len(t1+t2))
print(len(t))

#t3 = (1): Nope! 

#print("type tet", type(t3)) 
#int이므로 요소값이 하나일 때는 (1)로 하면 안되고 (1,)로 해야함


t3 = (1,2,3,4,5,6)
print(t3[:-1])

t4 = tuple(range(1,11)) #1~10까지
print(t4)

t5 = tuple(range(1,11,2)) #마지막은 간격: 1,3,5,7,9 
print(t5)

list4 = list(range(1,10))
print(list4)

#원소 in 시퀀스 확인 맞으면 true
print(1 in t2) 

#range, in, not in 시컨스(문자열, 튜플, 리스트)
print(1 not in t2)













































