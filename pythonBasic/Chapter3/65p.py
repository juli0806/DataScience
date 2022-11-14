#(1) 카운터와 누적변수
cnt=tot=0 # 변수 초기화
while cnt<5: #True ; loop
    cnt+=1 #counter var (cnt=cnt+1)
    tot+= cnt #sum var : tot=tot+cnt
    print(cnt,tot)

print('\nexercise 2')
#실습 1~100 사이 3의 배수 합과 원소 추출하기
cnt= tot =0
dataset =[] # empty

while cnt <100: # reply 100 times
    cnt+=1
    if cnt%3==0:
        tot+=cnt
        dataset.append(cnt)#append *******

print(f'1~100 사이 3의 배수 합 = {tot}')
print(f'dataset= {dataset}')