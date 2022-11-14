string="""식사는 없어 배고파도
음료는 없어 목말라도
달콤한 맛만 디저트만만 원하게 될 거 알잖아"""

sents=[] #sentences
words=[] #words

#(1) paragraph->sentences
for sen in string.split(sep="\n"):
    sents.append(sen)
    #(2) sentences->words
    for word in sen.split(): #sep=' '
        words.append(word)

print(f'sents: {sents}')
print(f'sents num:{len(sents)}')
print(f'words: {words}')
print(f'words num: {len(words)}')
