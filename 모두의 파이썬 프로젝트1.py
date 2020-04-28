#계산 맞히기 게임- 랜덤으로 사칙연산 문제를 보여줌,문제를 풀면 채점해서 점수 매기고 정답수를 알려줌
#eval함수 "3+5"로 문자열로 된 수식을 넣으면 수식처리해 계산값을 함수의 결과값으로 돌려줌

#프로젝트 구조
#사용자에게 제시할 문제를 만드는 함수 - randint 함수로 계산에 필요한 숫자 만든 후
# 덧셈 뺄셈 곱셈 중 하날 골라 문제 완성 / 함수를 실행해 만들어진 문제를 결괏값으로 돌려주는 함수

#메인 프로그램- 게임을 진행하는 부분으로 정답/오답 횟수를 기록하는 변수를 sc1,sc2를 초기화한후,
#문제만드는 함수를 호출해 문제를 만들고 사용자에게 보여준다. 그런 다음 사용자에게 입력을 받아
#정답과 오답을 판단하는 과정을 5번반복한다,

import random

def make_question():
    a = random.randint(1,40)
    b = random.randint(1,20)
    op = random. randint(1,3)

    #문자열 변수 q에 문제를 만든다. 그리고 첫번째 숫자를 q에 저장한다.
    q= str(a)

    #사칙연산을 추가한다
    if op ==1:
        q = q + "+"
    if op ==2:
        q = q + "-"
    if op==3:
        q = q + "*"

    #두 번째 숫자를 q에 저장한다.
    q = q+str(b)

    return q

#정답 / 오답 횟수를 저장할 변수 sc1과 sc2를 0으로 초기화 한다.

sc1 = 0
sc2 = 0

for x in range(5):
    q = make_question() #문제를 만듭니다.
    print(q)
    ans =input("=")
    r = int(ans)

    #컴퓨터가 계산한 결과인 eval(q)와 사용자 값(r)을 비교
    if eval(q) == r:
        print("정답")
        sc1 = sc1+1
    else:
        print("오답")
        sc2 = sc2 +1
print("정답",sc1,"오답",sc2)
