##윤년계산##

a = int(input("연도"))

b = a%4
c = a%100

if b==0 and c!=0:
    print("윤년")
else:
    print("음")
