
#50명의 승객과 매칭 기회, 총 탑승 승객 수 구하는 프로그램 작성
#승객별 운행 소요시간은 5~50분 사이의 난수
#소요시간 5~15분 사이의 승객만 매칭


import random

def taxi():
    people = {}
    for i in range(1,51):
        people[i] = random.randit(5,50)



    count = 0

    for key, value in people.items():
        if 5<= value <=15:
            check = "O"
            print(f"[{check}] {key}번째 손님 (소요시간 : {value})")
            count += 1
        else:
