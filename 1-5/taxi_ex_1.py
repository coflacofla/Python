import random
def taxi():
    people = {}
    for i in range(1, 51):
        people[i] = random.randint(5, 50)

    count = 0

    for key, value in people.items():
        if 5 <= value <= 15:
            check = "o"
            print(f"[{check}] {key}번째 손님 (소요시간 : {value})")
            count += 1
        else:
            check = " "
            print(f"[{check}] {key}번째 손님 (소요시간 : {value})")
    return count
print(f"총 탑승 승객 :", + taxi(), "분")
