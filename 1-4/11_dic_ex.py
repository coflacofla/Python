#단어장 

dictionary = {}

while True:
    word = input("영어 단어: ")
    
    if not word:
        
        break
    
    definition = input("뜻: ")
    
    dictionary[word] = definition



#퀴즈
    
print("\n퀴즈")


import random

correct = 0
wrong = 0


while True:
    q = random.choice(list(dictionary.keys()))

    print(q)

    a = input(f"{q}: ")
    
    
    if not a:
        break

    if a == dictionary[q]:
        correct += 1
    else:
        wrong += 1

total = correct + wrong

print(f"\n 맞은 개수/ 전체단어수 : {correct}/{total}")



