#함수란?  특정기능을 하는 프로그램을 작성후 이 부분을 정의하여 여러번 불러서
#사용 할수있게 하는 기능

#def 함수이름(인자-사용자가 함수를 호출시 함수에게 알려주는 정보)
#   함수내용
#   return 함수의 결과값  결과값생략가능 : 함수의 내용을 실행해서 얻는 정보

#인자가 있는 함수

def hello(name):
    print("Hello", name)

hello("Justin")
hello("peter")

def square(a):
    c= a*a
    return c

def triangle(a,h):
    c=a*h/2
    return c

s1 =4
s2= sqaure(s1) #s1의 제곱을 구하는 함수를 호출해 s2에 저장
print(s1,s2)

print(triangle(3,4)) #밑변이 3이고, 높이가 4인 삼각형의 넓이를 출력

#1부터 n까지의 합을 구하는 함수
def sum_func(n):
    s = 0 #합을 구하기위한 변수 s(시작값을 0으로 지정).
    for x in range(1, n+1): #range(1,n+1)로 n 까지를 반복
        s = s+x #s에 x를 계속 넣어 저장
        return s

    print(sum_func(10))
    print(sum_func(100))


#다각형을 그리는 함수

import turtle as t

def polygon(n):
    for x in range(n): #n번 반복한다.
        t.forward(50)
        t.left(360/n)

def polygon2(n,a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)

polygon(3)

t.up()  #거북이가 그림을 그리지 않도록 들고 100만큼 이동 다시 종이를 내린다. 
t.forward(100)
t.down()

polygon2(3,75)#한변이 75인 삼각형


