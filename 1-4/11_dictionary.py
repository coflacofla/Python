#딕셔너리
#연관된 값을 묶어서 저장
#키와 쌍으로 저장

dic0={'name':'이채림','phone':'000-0000-1111','birth':'0000909'}
print(dic0)
print(dic0['name'])

print()

dic0['name'] = 'Kaya'
print(dic0)

print()

#정보 삭제 delete = del
del dic0['name']
print(dic0)

print()

#keys() values() items() 함수
print(dic0.keys()) #키 정보를 list형태로 표현
print(dic0.values()) #값(정보)을 list형태로 표현
print(type(dic0.values()))
print(dic0.items()) #key와 value가 한 쌍으로 이루어진 형태로 불러

print()

for k, v in dic0.items():
    print(k,v)
print()

print(len(dic0))


