import random
import string

name = input('영어이름:')

#이름의 앞 3글자 추출
str1 = name[:3]

#3자리 난수 추출
str2 = str(random.randint(100,999))

id = str1 + str2

print(f'생성된 아이디:{id}')
