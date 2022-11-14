numData=[] # empty list

while True:
    num=int(input("input num: "))

    if num % 10 ==0: #condition
        print("programm exit")
        break
    else:
        print(num)
        numData.append(num) # list append