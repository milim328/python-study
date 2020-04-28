import random

n = random.randint(1,30) #1~30 사이에 있는 임의의 수를 뽑습니다. 

while True: # 영원히 반복합니다.
    x = input("맞춰보세요")
    g = int(x)  # 입력받은 값을 비교할수 있도록 정수로 바꾸기
    if g==n:    # 사용자가 추측한 값과 임의수가 같으면 정답
        print("정답")
        break
    if g < n:
        print("너무 작아요")
    if g > n:
        print("너무커요")
        
    
#단순하게 정해진 횟수를 반복할떄는 for명령문이 유용,
#반복을 계속할지 중단할지 조건을 판단하거나 무한반복을 해야할떄는 while 명령 유용
