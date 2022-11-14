#range () 함수 이용해 구구단 출력

#(1) outer for
for i in range(2,10):
    print (f'~~~{i}단~~~~')
    #(2) inner for
    for j in range(1,10):
        print(f'{i}*{j}={i*j}')
    print ("\n")