import datetime # datetime 클래스 사용
a = int(input("월을 입력하세요")) #사용자로부터 입력받기
b = int(input("일을 입력하세요"))

def solution(a,b):
    w = ["mon","tue","wed","thu","fri","sat","sun"]
    c = datetime.date(2016,a,b).weekday() #클래스 메서드 사용.. 숫자로 반환 되기 때문에
    
    return w[c] #요일 리스트 만들어서 c의 숫자 w의 요솟값으로 반환

print (solution(a,b))
