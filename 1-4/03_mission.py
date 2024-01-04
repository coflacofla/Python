s = 0

a = input("주민번호")


num1 = a.split('-')[0]
num2 = a.split('-')[1]

print(num1)
print(num2)


a1 = num1+num2

a2 = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]


for i in range(len(a2)):
    s=s+(int(a1[i])*a2[i])

print(s)

m1 = (s % 11)

m2 = 11 - m1
print(m2)
print(a1[12])

if m2==int(a1[12]):
    print("valid")
else :
    print("invalid")

