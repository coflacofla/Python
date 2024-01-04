list = ["영어","수학","파이썬"]

done = input("완료 과목:")

if done in list:
    print(f"완료된 과목: {done} \n {done}미션 완료")
    
else:
    print()


list.remove(done)
print(f"Updated To-Do List: \n {list}")


