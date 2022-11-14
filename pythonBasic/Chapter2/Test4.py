word1=input("첫번째 단어: ")
word2=input("두번째 단어: ")
word3=input("세번째 단어: ")
print('='*10)
initial=word1[:1]+word2[:1]+word3[:1]
#slicing할 필요 없이 [0]으로 접근
# + 연산자를 사용하면 메모리를 잡아먹으므로 format String을 쓰는 것이 좋다
print(f"약자: {initial}")