count=0
for i in range (int(input())):
    a=input()
    if '++' in a:
        count+=1
    else:
        count-=1
print(count)
