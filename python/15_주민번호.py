num = input("주민등록번호:")

num = num.split('-')[1]

code = int(num[1:3])

if 0<=code<=8 :
    print("서울입니다.")
elif 9<=code<=12:
    print("부산입니다.")
else :
    print("알 수 없습니다.")
