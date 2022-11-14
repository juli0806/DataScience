while True:
    num= int(input('홀수를 입력하세요 (0<-종료): '))

    if(num==0):
        print("마름모 프로그램 출력을 이용해 주셔서 감사합니다")
        break

    # up_row=int(num/2+1)
    # down_row=int(num/2)
    up_width=' '+('_'*num)
    down_width=' '+('-'*num)
    #
    print(up_width)
    #
    # for i in range(up_row): #행
    #     for j in range(up_row - i - 1): #공백
    #         if(j==0): print('|',end='')
    #         print(' ', end='')
    #     for k in range(2 * i + 1): # *
    #         if(j==up_row-i-1) and (k==0): print('|',end='')
    #         print('*', end='')
    #     for l in range(up_row - i - 1): #공백
    #         print(' ', end='')
    #     print('|')
    # for i in range(down_row):
    #     for j in range(i+1):
    #         if (j == 0): print('|', end='')
    #         print(' ',end='')
    #     for k in range(2*(down_row-i)-1):
    #         print('*',end='')
    #     for l in range(i+1):  # 공백
    #         print(' ', end='')
    #     print('|')
    #


    mid = int(num / 2)
    for i in range(num):
        if ((i * 2) + 1 <= num):
            print('|'+(' ' * mid), end='')
            print('*' * ((2 * i) + 1), end='')
            print(' ' * mid, end='')
            print('|')
            mid -= 1
        else:
            mid += 1
            print('|'+(' ' * (mid + 1)), end='')
            print('*' * ((num - i) * 2 - 1), end='')
            print(' ' * (mid + 1), end='')
            print('|')

    print(down_width)