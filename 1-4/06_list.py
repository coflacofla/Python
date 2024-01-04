#리스트

list1=[1,2,3,4]
list2 = ['인재영', '이채림', '장현준']
list3 = [1,2,3,4.5,'a','b']
list4 = [[1,2,3],'a']

print(list4)
print(list4[0])
print(list2[1])
#리스트 속 리스트의 인덱싱
print(list4[0][2])


print(list4[-1])
print(list4[-2])
print(list4.index('a'))
print(list2.index('인재영'))

#list의 append를 이용하여 data 추가하기

list2.append('문정현')
list2.append('배한결')
list2.append('김준화')

print(list2)

#insert함수 사용하기 : 위치도 지정

list3.insert(0,'#') #가장 앞자리에 # 넣기 
print(list3)

#remove함수 사용하기
list3.remove('#') #요소 
print(list3)
#pop함수 사용해서도 뺄 수 있다
list4.pop(1) #인덱스값
print(list4)


