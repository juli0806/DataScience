var=10 #if 블럭에서 사용될 변수
var=10
#들여쓰기(Indentation)으로 블럭을 표현
""" #여러줄 주석의 효과
if var >=5 : #조건식
    print('var=', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')
"""

print('항시실행')
# if var >=5 : #조건식
if var >= 100:
    print('var=', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')

#if 이하의 블럭은 동일한 들여쓰기 개수로 작성해야한다
#jaejollim