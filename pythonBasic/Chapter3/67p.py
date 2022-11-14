#
print("(1) add random module ")

import random
help(random) #module help

#
print("(2) module function help")
help(random.random)

#
print("(3) random num between 0~1")
r=random.random()
print(f'r={r}')

#
print("[practice] if the rand num is under 0.01, exit and print the number of rand num")
cnt=0
while True:
    r=random.random()
    print(random.random())
    if r < 0.01:
        break # loop exit
    else:
        cnt+=1

print(f'난수개수={cnt}')
