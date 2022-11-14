import random

print("이름 list에 전체 이름, 특정 이름 출력")
names=['홍길동','이순신','유관순']
print(names)
print(names[2])

print("-------------")
print("list 에서 자료 유무 확인하기")
if '유관순' in names:
    print('presence ')
else:
    print('absence')



print("-------------")
print("난수 정수로 이름 선택하기")
idx= random.randint(0,2)
print(f'random={idx}')
print(names[idx])