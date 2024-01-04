##금액에 따른 할인율 계산##

a = int(input("물건 구매가를 입력하세요:"))

print(f"구매가: {a}")

b= 5
c = 7.5
d = 10

if 10000<=a<50000:
    f = a*0.95
    print(f"할인율:{b}%")
elif 50000<=a<100000:
    f = a*0.925
    print(f"할인율: {c}%")
elif a>=100000:
    f = a*0.9
    print(f"할인율: {d}%")

dis = int(a-f)
pri = int(f)

print(f"할인금액: {dis}")
str ='할인금액:{}'.format(dis)
print(str)
print(f"지불금액: {pri}")

