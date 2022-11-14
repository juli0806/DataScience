print("#Type A")
vector_a_num=int(input("vector 수: "))
lst_a=[]
lst_a_index=0
while(lst_a_index<vector_a_num):
    lst_a.insert(lst_a_index,int(input("")))
    lst_a_index+=1

print(lst_a)
print(len(lst_a))

print()
print("#Type B")
vector_b_num=int(input("vector 수: "))
lst_b=[]
lst_b_index=0
while(lst_b_index<vector_b_num):
    lst_b.insert(lst_b_index,int(input("")))
    lst_b_index+=1

search_num=int(input(""))

if (search_num in lst_b):
    print("YES")
else:
    print("NO")


