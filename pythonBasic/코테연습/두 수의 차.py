def solution(num1, num2):
    answer = 0
    if (num1 <= 50000 and num1 >= -50000) and (num2 <= 50000 and num2 >= -50000):
        answer=num1 - num2

    return answer

print(solution(10,5))