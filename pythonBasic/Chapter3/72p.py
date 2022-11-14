print("make range obj")

num1=range(10) #start
print(f"num1:{num1}")
num2=range(1,10) #start,end
print(f"num2:{num2}")
num3=range(1,10,2) #start,end,step
print(f"num3:{num3}")

print("use range obj")
for n in num1:
    print(n,end=' ')
print()
for n in num2:
    print(n,end=' ')
print()
for n in num3:
    print(n,end=' ')
print()
