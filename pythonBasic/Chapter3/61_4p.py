#100~85: '우수', 84~70: '보통', 69 이하: '저조'
score=int(input('점수 입력 : '))
if score>=85 and score<=100:
    print('우수')
elif score>=70 and score<85:
    print('보통')
elif score >=0 and score < 70:
    print('저조')
else:
    print('저조')