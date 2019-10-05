n=input()
a=input()
count,count_=0,0
for i in (a):
    if i=='A':
        count+=1
    else:
        count_+=1
if (count==count_):print('Friendship')
else:
    print(('Anton','Danik')[count<count_])
