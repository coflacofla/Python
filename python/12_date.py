min = int(input("분: "))

#3000min
#/60 =50hrs
#/24 = days


day = min//(60*24)


hour = min%(60*24)//60

min = min - day * 60 * 24 -hour *60

print(f'분을 입력 :: {min}')
print(f'{day}일 {hour}시간 {min}분 입니다.')
