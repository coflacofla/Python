### 1. 함수

#함수 선언
def say():#이건 변수 없는 함수
    print("~~여기는 파이썬 수업~~")
    
def sayhello(name, birthyear):#여기 있는 변수가 매개 변수
    print("",name,"님.. 안녕하세요") #",name,"해도 되고, 그냥 name+해도 되고
    print("올해 나이는",birthyear,"살 입니다.")
    print("파이썬 과정에 오신 것을 환영합니다.\n")
#함수 호출
#호출이 먼저 나올 경우 위에서부터 실행되기 때문에 문제가 생긴다.함수 선언은 위에 몰아서 하기
#여기 있는 변수는 보통 인수로 부름

##sum구하는 함수(값을 return하는 함수)
def get_sum_return(n1,n2):
    r = n1+n2
    return r


##더하기와 빼기 연산을 하는 함수
def get_plus_min(n1, n2):
    p = n1+n2
    m = n1-n2
    return p, m
    return m #위에서 이미 return해서 이 줄은 무시함 ,로 이어서 써야함


##값을 입력하면 홀짝 구분하는 함수
def is_odd_even(n):
    if n == 0:
        return 0
    elif n%2 == 0:
        return "짝수"
    else:
        return "홀수"



##default인수를 받는 함수
#프린트 구문에서 end를 안받으면 알아서 줄바꿈이지만 직접 지정도 가능한 그런거

def greet(name, msg = '반가워'):
    #'반가워'가 default로 들어가 있어서 msg입력을 안해도된다
    print(f"{name}씨에게...{msg}")



##키워드 인수를 받는 함수
def get_minus(x, y, z):
    r = x - y + z
    return r


#이렇게 적으면 내가 원하는 순서로 값을 입력받게 됨
#키워드나 디폴트 인수는 꼭 뒤에 적어야함. 앞에 오면 포지션 오류뜸

##함수의 정의, 인수값 확인하는 법

##가변인수 (*달면 가변 인수. 보통 *args라고쓴다)
def param1(*args):
    print(args)


#**달면 딕셔너리 형태로(키베이스로) 가변 인수를 쓸 수 있다. 보통 **kargs라고 씀
def param2(**kargs):
    print(kargs)


##전역 변수(여러 함수에서 같은 값을 쓰는 경우)
a = 1
b = 0
def fun1():
    b = 2
    print(a, b)
def fun2():

    global b
    print(a,b)
#지역변수 b가 따로 있어서 바깥의 b에 영향받지 않음
#전역변수 b를 사용하기 때문에 바깥의 b값을 가져옴

####Q.쿠폰으로 주스 마시기####

def free(n, myk):
    k = myk
    juice = 0
    for i in range(1, myk+1):
        if k >= n:
            k -= n
            juice += 1
            k +=1
        else :
            print("영일이는 {}잔을 무료로 마시고 쿠폰 {}장이 남습니다.".format(juice, k))
            break
    


