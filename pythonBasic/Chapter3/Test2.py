import random
print('숫자 맞추기 게임')
com=random.randint(1,10) #1~10 사이 난수 정수 발생

while True:
     my=int (input('예상 숫자를 입력하시오: ')) # 숫자 입력
     if my>com:
         print('더 작은 수 입력')
         continue
     elif my<com:
         print('더 큰 수 입력')
         continue
     else:
         print('~~~정답~~~~')
         break

