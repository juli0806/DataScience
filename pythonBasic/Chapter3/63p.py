# (1) general condicion
num=9 #initialize
result=0
#recommanded
if num >= 5:
    result=num * 2
else:
    result=num + 2

print(f'result={result}')#18
#just for comprehend
#(2) ternary opetator
# form) var= false if (condition) else false
result2= num * 2 if num >= 5 else num+2
print(f'result2={result2}') #18