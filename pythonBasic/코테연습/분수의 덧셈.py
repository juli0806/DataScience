def solution(denum1, num1, denum2, num2):  # de: 분자 num: 분모
    answer = []
    de = num2 * denum1 + num1 * denum2
    num = num1 * num2

    i = 1
    while (i <= num):
        if (de % i == 0 and num % i == 0):
            gcf = i
        i += 1

    de /= gcf
    num /= gcf
    answer.append(int(de))
    answer.append(int(num))
    return answer

print(solution(1,2,3,4))
