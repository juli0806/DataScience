list = []
sum=0

for num in range(100):
    if(num%3==0) and (num%2!=0):
        list.append(num)
        sum+=num

print(f'수열: {list}')
print(f'합:{sum}')