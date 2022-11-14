# 7.	공원 요금 계산 프로그램 ver2
# 나이를 입력 받아 나이에 따른 더조은 IT공원 등급,입장료를 계산 하는 프로그램을 작성하시오.
#
# 0~3세(유아):무료
# 4~13세(어린이): 2000원
# 14~18세(청소년): 3000원
# 19~65세(성인): 5000원
# 66세 이상(노인): 무료

while True:
    fee=0
    age=int(input('나이를 입력하세요 '))
    if(age>=19 and age<=65):
        grade='성인'
        fee=5000
    elif (age>=14 and age<=18):
        grade='청소년'
        fee=3000
    elif (age>=4 and age<=13):
        grade='어린이'
        fee=2000
    elif (age>=66):
        grade='노인'
    elif (age<=3 and age>=0):
        grade='유아'
    else:
        print('다시 입력하세요\n')
        continue

    if(fee!=0):
        print(f'귀하는 {grade} 등급이며 요금은 {fee}원 입니다')
    else:
        print(f'귀하는 {grade} 등급이며 요금은 무료입니다')