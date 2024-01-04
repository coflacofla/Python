#홀수인지 짝수인지
#a = int(input("숫자입력"))

'''
#if~else
if a%2==0:
    print("even")
else:
    print("odd")

#if elif else 구조
money = int(input("가격 : "))
if money >=5000:
    print("taxi")
elif 2300<=money<5000:
    print("bus")
else:
    print("subway")
'''

money = int(input("가격"))

card = False

if money >=5000 or card:
    print("taxi")
elif 2300<=money<5000:
    print("bus")
else:
    print("subway")

print("taxi") if money >=5000 or card else print("bus") if 2300<=money<5000 else print("subway")

    
'''
#[True] if [조건식] else [ False]

print("even")if a%2 == 0 else print("odd")

'''
