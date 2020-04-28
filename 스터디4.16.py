#소수찾기 : 
#순열 n!/(n-r)! 중 소수찾기. 11과 011을 같은 숫자로 취급하게 하기, 문자열-split하기, 
#팩토리얼 정의하기
def factorial(n):
    answer =1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1):
            answer += answer*i
        return answer
def permu(n,r):
    return factorial(n) / factorial(n-r)

def solution(numbers):
    answer=0, list(numbers)
#숫자조합 만들기 : 순열사용
for 문으로 순열 사용 그리고 set 으로 중복 제거

#소수찾기 - 에라토스테네스의 체????
#1.1 부터 n 까지의 자연수를 전부 나열한다.
#2. 소수도, 합성수도 아닌 1을 지운다.
#3. 남아 있는 자연수 중 가장 작은 수인 2는 소수다. 이제 2의 배수들을 모두 지운다.
#4. 남아 있는 자연수 중 가장 작은 수인 3은 소수다. 이제 3의 배수들을 모두 지운다.
#5. 남아 있는 자연수 중 가장 작은 수는 소수다. 이 수의 배수들을 모두 지운다.
#6. 남은 자연수 중 가장 작은 수가 의 제곱근을 넘을 때까지 과정 5를 반복하면, 남아 있는 수가 모두 소수다.

#스터디결과 :  7자리 숫자받아서 리스트화 해주기
#스트링을 인트로 바꾸기
#순열사용
#1~7자리까지 반복문 사용
#0을 없애기 위해서는 조합후 int 형으로 append
#set으로 중복제거, 그리고 소수찾기




  



#모의고사 1차배열- 학생클래스를 만들어서 학생 1,2,3의 답안지를 만든다
#그리고 답지를 만들어서 맞으면 리스트를 생성하는 함수 만들기
#학생 1,2,3 을 만들어서 

import random
m=0
class student:
    def_init_(self):
        stu_ans = []
        stu_ans=list()
        for i in range(1,m):
            stu_ans.append(rand.randint(1,5))
def solution():
    answers = []
    ans_list =[]
    i=0
    n=0
    while n < m :
        if(answers[n] == stu_ans[n]):
            ans_list.append(i+=1)
    return ans_list

#모의고사 문제 - 틀린이유: 찍는 방식이 있었음
1.위너 설정
2.패턴으로 리스트 3개를 짜고, 스코어 설정=0
3.패턴을 답지수만큼 늘리기
4.for i in ranage(len(answer))로 if해서 맞은 사람에게 스코어 1추가
5.max 가려내기 - 그리고 오름차순

