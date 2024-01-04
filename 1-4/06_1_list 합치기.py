#list 합치기

list1=[1,2,3,4]
list2 = ['인재영', '이채림', '장현준']
list3 = [1,2,3,4.5,'a','b']
list4 = [[1,2,3],'a']

list1.extend(list2)
print(list1)

print(list1+[7,8,9])

import random

menu = ["떡볶이","뚝불","짜장면","김밥","돈까스","햄버거"]

print("오늘의 메뉴는?",random.choice(menu))

#print(dir(list)) #dir: list 제공 함수들 보여주는 함수

list2.sort() #문자형만 가능....?

print(list2)

menu.sort()
print(menu)

