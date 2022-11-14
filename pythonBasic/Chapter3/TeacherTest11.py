while True:
    num= int(input('홀수를 입력하세요 (0<-종료): '))
    if(num==0):
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다")
        break
    row=int(num/2+1)
    for i in range(row):
        for j in range(row - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print('*', end='')
        print('')