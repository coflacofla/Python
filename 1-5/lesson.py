def say():
    print("python class")

def sayhello(name, birthyear):
    print(name+"..hello")
    print("age: 2024-birthyear")
    print("welcome to python class \n")


def get_sum(n1,n2):
    r = n1+n2
    return r

def get_plus_min(n1,n2):
    p = n1+n2
    m = n1-n2
    return p,m

def odd_even(n):
    if n == 0:
        return 0
    elif n%2 == 0:
        return "짝수"
    esle:
        return "홀수"

def greet(name, msg='반가워'):
    print(f"{name}씨에게 {msg})

def get_minus(x,y,z):
    r = x - y + z
    return r

def param1(*arg):
    print(args)

def param2(**kargs):
    print(kargs)


a = 1
b = 0

def fun1():
    b=2
    print(a,b)
def fun2():
    global b
    print(a,b)

















