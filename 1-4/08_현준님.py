td_list = ["영어", "수학", "파이썬"]

def print_list(a) :
    print("To-Do List:")
    for i in range(0, len(a)) :
        print(f"- {a[i]}")

print_list(td_list)

fin = input("완료된 과목: ")
td_list.remove(fin)
print(f"{fin} 미션 완료\n")

print("Updated ", end="")
print_list(td_list)
