multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다"""

words=[] #단어저장

for word in multiline.split():
    words.append(word)

num=len(words)
for i in range(num):
    print(words[i])
print(f'단어개수: {num}')