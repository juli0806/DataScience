#100~85: '우수', 84~70: '보통', 69 이하: '저조'
score=int(input('점수 입력 : '))
grade=''\
    ''

if score>=85 and score<=100:
    print('우수')
else:
    if score>=70:
        print('보통')
    else:
        print('저조')


print('당신의 점수는 %d이고 등급은 %s',{score,grade})