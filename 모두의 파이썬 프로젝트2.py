#타자게임
#게임이 시작되면 동물 이름으로 된 영어 단어가 화면에 표시됩니다.----리스트사용/랜덤함
#사용자는 그 단어를 최대한 빠르고 정확하게 입력해야 합니다. 바르게 입력했으면 다음 문제로 넘어가고,
#오타가 있으면 같은 단어가 한 번 더 나옵니다.
#틀린 문제를 다시 입력하는 동안에도 시간은 계속 흐르기 때문에 속도뿐만 아니라
#정확도도 중요한 게임입니다.

#사전준비 - 게임에 필요한 모듈을 임포트

#메인프로그램 :타자게임을 처리하는 부분 -- 사용자에게 문제 보여주고 타자 입력을
#받아 반복 -- 오타가 나면 계속해야하므로 while 사용

#결과 계산해서 보여주기 : 타자를 입력한 시간을 소수점 둘째 자리까지 계산해서 출력

import time
import random

#단어 리스트 작성
w = ["cat", "dog", "fox","monkey","mouse","panda","frog","snake","wolf"]
n=1 #문제번호

print("타자게임- 준비되면 엔터")
input()
start = time.time() #시작시간을 기록한다.

q= random.choice(w)
while n <= 5:
    print("문제",n)
    print(q)
    x= input()
    if q == x:
        print("통과!")
        n = n+1
        q = random.choice(w)
    else:
        print("오타 : 재입력")

end = time.time()
et = end - start
et = format(et, ".2f") #보기좋게 소수점 2째자리까지 표기 , format 사용
print("타자시간:", et, "초")
