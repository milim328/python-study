def solution(a, b):
    answer = 0
    for n in range(a,b+1):
        answer += n
    return answer
print(solution(3,5))

