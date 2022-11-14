message_a=['spam','ham','spam','ham','spam']
message_b=['spam','ham','spam','ham','spam']

print("Type A")
for i in range(len(message_a)):
    if message_a[i]=='spam':
        message_a[i]=1
    elif message_a[i]=='ham':
        message_a[i]=0

print(message_a)

print("Type B")
spam_list=[]
for i in message_b:
    if i=='spam':
        spam_list.append(i)
print(spam_list)