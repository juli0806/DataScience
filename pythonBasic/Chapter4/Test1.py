lst=[10,1,5,2,10,1,5,2]

#step1
result=lst*2
print(result)

#step2
result.insert(0,lst[0]*2)
print(result)

#step3
result2=[i for i in result[::2]]
print(result2)